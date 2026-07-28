#!/usr/bin/env python3
"""Validate linked PCC evidence registers using only the Python standard library."""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Dict, List, Mapping, Tuple

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "registers.json"

STRONG_NOVELTY_RE = re.compile(
    r"\b(first(?:-ever)?|unprecedented|no prior work|never before|world['’]?s first)\b",
    re.IGNORECASE,
)

ALLOWED_METADATA_AUTHORITIES = {
    "zotero", "provisional_elicit", "manual_verified", "unknown"
}

ALLOWED_PROTOTYPE_EVIDENCE_TYPES = {
    "implementation", "test", "machine_readable_output", "metric", "limitation"
}
ALLOWED_CONTEXT_CONDITIONS = {
    "not_applicable", "zero_context", "partial_context", "full_context", "mixed"
}
ALLOWED_PROTOTYPE_VERIFICATION_STATUSES = {
    "planned", "recorded_unverified", "reproduced", "verified", "superseded"
}
ALLOWED_CLAIM_PROTOTYPE_RELATIONS = {
    "IMPLEMENTS", "DEMONSTRATES", "TESTS", "PARTIALLY_OPERATIONALIZES",
    "ESTABLISHES_LIMITATION", "DOES_NOT_YET_EVALUATE",
}
ALLOWED_WORDING_CEILINGS = {
    "implementation_only", "controlled_synthetic_demonstration",
    "current_benchmark_result", "limitation_only", "future_work_only",
}
ALLOWED_SECTION_CLAIM_ROLES = {
    "definition", "theoretical_support", "construct", "method", "implementation",
    "result", "limitation", "scope", "novelty",
}
ALLOWED_SECTION_TRACEABILITY_STATUSES = {
    "planned", "mapped", "comment_inserted", "reviewed", "superseded"
}
PROTOTYPE_ELIGIBLE_CLAIM_TYPES = {
    "implementation", "methodological", "empirical", "scope", "limitation"
}
IMMUTABLE_COMMIT_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


def is_valid_date(value: str) -> bool:
    if not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def read_csv(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def split_ids(value: str) -> List[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def validate_novelty_wording(row: Mapping[str, str]) -> List[str]:
    status = (row.get("audit_status") or "").strip().lower()
    wording = row.get("current_wording") or ""
    if status != "supported" and STRONG_NOVELTY_RE.search(wording):
        return [
            f"{row.get('novelty_id','<unknown>')}: unsupported novelty status "
            f"{status!r} uses strong priority wording: {wording!r}"
        ]
    return []


def validate_prototype_evidence(row: Mapping[str, str]) -> List[str]:
    """Validate one prototype record without contacting its repository."""
    record_id = row.get("prototype_evidence_id", "<unknown>")
    errors: List[str] = []
    evidence_type = (row.get("evidence_type") or "").strip()
    context = (row.get("context_condition") or "").strip()
    status = (row.get("verification_status") or "").strip()
    for field, value, allowed in (
        ("evidence_type", evidence_type, ALLOWED_PROTOTYPE_EVIDENCE_TYPES),
        ("context_condition", context, ALLOWED_CONTEXT_CONDITIONS),
        ("verification_status", status, ALLOWED_PROTOTYPE_VERIFICATION_STATUSES),
    ):
        if value not in allowed:
            errors.append(f"{record_id}: unsupported {field} {value!r}")

    if status in {"reproduced", "verified"}:
        for field in (
            "prototype_repository", "code_path", "symbol_or_test", "execution_command",
            "observed_result", "limitations", "verified_date",
        ):
            if not (row.get(field) or "").strip():
                errors.append(f"{record_id}: {status} record lacks {field}")
        commit = (row.get("commit_sha") or "").strip()
        if not IMMUTABLE_COMMIT_RE.fullmatch(commit):
            errors.append(f"{record_id}: {status} record has invalid immutable commit_sha {commit!r}")
        date = (row.get("verified_date") or "").strip()
        if date and not is_valid_date(date):
            errors.append(f"{record_id}: invalid verified_date {date!r}; expected YYYY-MM-DD")
        if evidence_type in {"machine_readable_output", "metric"} and not (
            row.get("output_artifact") or ""
        ).strip():
            errors.append(f"{record_id}: {evidence_type} {status} record lacks output_artifact")
    return errors


def validate_claim_prototype_link(row: Mapping[str, str]) -> List[str]:
    link_id = row.get("link_id", "<unknown>")
    errors: List[str] = []
    relation = (row.get("relation") or "").strip()
    ceiling = (row.get("wording_ceiling") or "").strip()
    if relation not in ALLOWED_CLAIM_PROTOTYPE_RELATIONS:
        errors.append(f"{link_id}: unsupported relation {relation!r}")
    if ceiling not in ALLOWED_WORDING_CEILINGS:
        errors.append(f"{link_id}: unsupported wording_ceiling {ceiling!r}")
    return errors


def validate_section_claim_map(row: Mapping[str, str]) -> List[str]:
    map_id = row.get("map_id", "<unknown>")
    errors: List[str] = []
    role = (row.get("claim_role") or "").strip()
    status = (row.get("traceability_status") or "").strip()
    if role not in ALLOWED_SECTION_CLAIM_ROLES:
        errors.append(f"{map_id}: unsupported claim_role {role!r}")
    if status not in ALLOWED_SECTION_TRACEABILITY_STATUSES:
        errors.append(f"{map_id}: unsupported traceability_status {status!r}")
    if status in {"comment_inserted", "reviewed"}:
        for field in ("proposal_repository", "proposal_commit_sha", "proposal_path", "section_anchor"):
            if not (row.get(field) or "").strip():
                errors.append(f"{map_id}: {status} mapping lacks {field}")
    reviewed = (row.get("last_reviewed") or "").strip()
    if reviewed and not is_valid_date(reviewed):
        errors.append(f"{map_id}: invalid last_reviewed {reviewed!r}; expected YYYY-MM-DD")
    return errors


def validate_all(root: Path = ROOT) -> Tuple[List[str], Dict[str, int]]:
    errors: List[str] = []
    counts: Dict[str, int] = {}

    schema = json.loads((root / "schema" / "registers.json").read_text(encoding="utf-8"))
    patterns = {name: re.compile(pattern) for name, pattern in schema["id_patterns"].items()}

    rows_by_path: Dict[str, List[Dict[str, str]]] = {}
    ids_by_path: Dict[str, set[str]] = {}

    for rel_path, spec in schema["registers"].items():
        path = root / rel_path
        if not path.exists():
            errors.append(f"missing required register: {rel_path}")
            continue

        headers, rows = read_csv(path)
        rows_by_path[rel_path] = rows
        counts[rel_path] = len(rows)

        missing = [col for col in spec["required_columns"] if col not in headers]
        if missing:
            errors.append(f"{rel_path}: missing columns {missing}")

        id_col = spec["id_column"]
        pattern = patterns[spec["id_pattern"]]
        seen: set[str] = set()
        for line_no, row in enumerate(rows, start=2):
            value = (row.get(id_col) or "").strip()
            if not value:
                errors.append(f"{rel_path}:{line_no}: empty {id_col}")
                continue
            if not pattern.fullmatch(value):
                errors.append(f"{rel_path}:{line_no}: invalid {id_col} {value!r}")
            if value in seen:
                errors.append(f"{rel_path}:{line_no}: duplicate {id_col} {value!r}")
            seen.add(value)
        ids_by_path[rel_path] = seen

    required_sets = [
        "data/components.csv", "data/claims.csv", "data/sources.csv",
        "data/novelty_propositions.csv", "data/searches.csv", "data/decisions.csv"
    ]
    if any(path not in ids_by_path for path in required_sets):
        return errors, counts

    components = ids_by_path["data/components.csv"]
    claims = ids_by_path["data/claims.csv"]
    sources = ids_by_path["data/sources.csv"]
    novelty = ids_by_path["data/novelty_propositions.csv"]
    searches = ids_by_path["data/searches.csv"]
    decisions = ids_by_path["data/decisions.csv"]
    imports = ids_by_path.get("imports/manifest.csv", set())
    prototype_evidence = ids_by_path.get("data/prototype_evidence.csv", set())

    def check_fk(rel_path: str, column: str, valid: set[str], multi: bool = False) -> None:
        for line_no, row in enumerate(rows_by_path.get(rel_path, []), start=2):
            values = split_ids(row.get(column, "")) if multi else [row.get(column, "").strip()]
            for value in values:
                if value and value not in valid:
                    errors.append(f"{rel_path}:{line_no}: {column} references unknown ID {value!r}")

    check_fk("data/components.csv", "decision_id", decisions)
    check_fk("data/claims.csv", "components", components, multi=True)
    check_fk("data/claim_source_links.csv", "claim_id", claims)
    check_fk("data/claim_source_links.csv", "source_id", sources)
    check_fk("data/claim_decision_links.csv", "claim_id", claims)
    check_fk("data/claim_decision_links.csv", "decision_id", decisions)
    check_fk("data/component_provenance.csv", "component_id", components)
    check_fk("data/component_provenance.csv", "source_id", sources)
    check_fk("data/novelty_propositions.csv", "components_combined", components, multi=True)
    check_fk("data/novelty_propositions.csv", "searches_completed", searches, multi=True)
    check_fk("data/novelty_source_links.csv", "novelty_id", novelty)
    check_fk("data/novelty_source_links.csv", "source_id", sources)
    check_fk("imports/manifest.csv", "duplicate_of", imports)
    check_fk("data/claim_prototype_links.csv", "claim_id", claims)
    check_fk("data/claim_prototype_links.csv", "prototype_evidence_id", prototype_evidence)
    check_fk("proposal/section_claim_map.csv", "claim_id", claims)

    linked_claims = {r["claim_id"] for r in rows_by_path.get("data/claim_source_links.csv", [])}
    decision_linked = {r["claim_id"] for r in rows_by_path.get("data/claim_decision_links.csv", [])}
    prototype_linked = {
        r["claim_id"] for r in rows_by_path.get("data/claim_prototype_links.csv", [])
    }
    for line_no, row in enumerate(rows_by_path.get("data/claims.csv", []), start=2):
        cid = row["claim_id"]
        prototype_suffices = (
            cid in prototype_linked
            and (row.get("claim_type") or "").strip() in PROTOTYPE_ELIGIBLE_CLAIM_TYPES
        )
        if cid not in linked_claims and cid not in decision_linked and not prototype_suffices:
            errors.append(f"data/claims.csv:{line_no}: {cid} has no source or decision link")

    for row in rows_by_path.get("data/prototype_evidence.csv", []):
        errors.extend(validate_prototype_evidence(row))
    for row in rows_by_path.get("data/claim_prototype_links.csv", []):
        errors.extend(validate_claim_prototype_link(row))
    for row in rows_by_path.get("proposal/section_claim_map.csv", []):
        errors.extend(validate_section_claim_map(row))

    for line_no, row in enumerate(rows_by_path.get("data/sources.csv", []), start=2):
        authority = (row.get("metadata_authority") or "").strip()
        if authority not in ALLOWED_METADATA_AUTHORITIES:
            errors.append(
                f"data/sources.csv:{line_no}: unsupported metadata_authority {authority!r}"
            )
        if authority == "zotero" and not (row.get("zotero_key") or "").strip():
            errors.append(
                f"data/sources.csv:{line_no}: Zotero-authoritative record lacks zotero_key"
            )

    for row in rows_by_path.get("data/novelty_propositions.csv", []):
        errors.extend(validate_novelty_wording(row))

    canonical_by_hash: Dict[str, List[Tuple[int, Dict[str, str]]]] = defaultdict(list)
    for line_no, row in enumerate(rows_by_path.get("imports/manifest.csv", []), start=2):
        sha = (row.get("sha256") or "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            errors.append(f"imports/manifest.csv:{line_no}: invalid SHA-256 {sha!r}")
        canonical_by_hash[sha].append((line_no, row))
        status = (row.get("import_status") or "").strip()
        if status == "included":
            stored = (row.get("stored_path") or "").strip()
            if not stored:
                errors.append(f"imports/manifest.csv:{line_no}: included import lacks stored_path")
            elif not (root / stored).exists():
                errors.append(
                    f"imports/manifest.csv:{line_no}: stored raw file is missing: {stored}"
                )
    for sha, grouped in canonical_by_hash.items():
        if len(grouped) <= 1:
            continue
        canonical = [
            row for _, row in grouped
            if row.get("import_status") in {
                "included", "checksum_recorded_pending_binary_import", "external_baseline_only"
            } and not row.get("duplicate_of")
        ]
        duplicates = [row for _, row in grouped if row.get("duplicate_of")]
        if len(canonical) != 1:
            errors.append(
                f"imports/manifest.csv: hash {sha} must have exactly one canonical record"
            )
        if len(duplicates) != len(grouped) - 1:
            errors.append(
                f"imports/manifest.csv: duplicate hash {sha} has an unmarked duplicate record"
            )

    return errors, counts


def main() -> int:
    errors, counts = validate_all()
    if errors:
        print("PCC register validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    total = sum(counts.values())
    print(f"PCC register validation passed: {len(counts)} registers, {total} rows.")
    for path, count in sorted(counts.items()):
        print(f"- {path}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
