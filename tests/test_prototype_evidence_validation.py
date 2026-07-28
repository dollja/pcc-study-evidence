from __future__ import annotations

import csv
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_registers import ROOT, validate_all


class PrototypeEvidenceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repository"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.temporary.cleanup()

    def append(self, path: str, row: dict[str, str]) -> None:
        csv_path = self.root / path
        with csv_path.open("r", encoding="utf-8", newline="") as handle:
            fields = next(csv.reader(handle))
        with csv_path.open("a", encoding="utf-8", newline="") as handle:
            csv.DictWriter(handle, fieldnames=fields).writerow(row)

    def add_pev(self, **overrides: str) -> None:
        row = {
            "prototype_evidence_id": "PEV-9999",
            "revision_batch": "INFRA-PEV-001",
            "prototype_repository": "example/prototype",
            "commit_sha": "a" * 40,
            "evidence_type": "implementation",
            "scenario_id": "scenario-placeholder",
            "context_condition": "not_applicable",
            "code_path": "example.py",
            "symbol_or_test": "example_symbol",
            "execution_command": "python example.py",
            "output_artifact": "",
            "observed_result": "placeholder observed result",
            "verification_status": "reproduced",
            "limitations": "placeholder limitation",
            "verified_date": "2026-07-28",
        }
        row.update(overrides)
        self.append("data/prototype_evidence.csv", row)

    def errors(self) -> list[str]:
        return validate_all(self.root)[0]

    def assert_error_contains(self, text: str) -> None:
        errors = self.errors()
        self.assertTrue(any(text in error for error in errors), "\n".join(errors))

    def test_real_repository_validates_with_header_only_registers(self):
        errors, _ = validate_all()
        self.assertEqual([], errors, "\n".join(errors))

    def test_new_register_paths_appear_in_counts(self):
        _, counts = validate_all()
        for path in (
            "data/prototype_evidence.csv",
            "data/claim_prototype_links.csv",
            "proposal/section_claim_map.csv",
        ):
            self.assertIn(path, counts)
            self.assertEqual(0, counts[path])

    def test_invalid_pev_id_is_rejected(self):
        self.add_pev(prototype_evidence_id="PEV-99")
        self.assert_error_contains("invalid prototype_evidence_id")

    def test_abbreviated_commit_is_rejected_for_reproduced_record(self):
        self.add_pev(commit_sha="abc1234")
        self.assert_error_contains("invalid immutable commit_sha")

    def test_malformed_commit_is_rejected_for_reproduced_record(self):
        self.add_pev(commit_sha="G" * 40)
        self.assert_error_contains("invalid immutable commit_sha")

    def test_reproduced_record_requires_execution_command(self):
        self.add_pev(execution_command="")
        self.assert_error_contains("lacks execution_command")

    def test_reproduced_record_requires_limitations(self):
        self.add_pev(limitations="")
        self.assert_error_contains("lacks limitations")

    def test_reproduced_metric_requires_output_artifact(self):
        self.add_pev(evidence_type="metric", output_artifact="")
        self.assert_error_contains("metric reproduced record lacks output_artifact")

    def test_claim_prototype_link_rejects_unknown_claim(self):
        self.add_pev()
        self.add_link(claim_id="CLM-9999")
        self.assert_error_contains("claim_id references unknown ID 'CLM-9999'")

    def test_claim_prototype_link_rejects_unknown_prototype_evidence(self):
        self.add_link(prototype_evidence_id="PEV-9998")
        self.assert_error_contains("prototype_evidence_id references unknown ID 'PEV-9998'")

    def add_link(self, **overrides: str) -> None:
        row = {
            "link_id": "CPE-9999", "claim_id": "CLM-0002",
            "prototype_evidence_id": "PEV-9999", "relation": "IMPLEMENTS",
            "wording_ceiling": "implementation_only", "notes": "test fixture",
        }
        row.update(overrides)
        self.append("data/claim_prototype_links.csv", row)

    def test_unsupported_relation_is_rejected(self):
        self.add_pev()
        self.add_link(relation="PROVES")
        self.assert_error_contains("unsupported relation 'PROVES'")

    def test_unsupported_wording_ceiling_is_rejected(self):
        self.add_pev()
        self.add_link(wording_ceiling="generalized")
        self.assert_error_contains("unsupported wording_ceiling 'generalized'")

    def remove_existing_links(self, claim_id: str) -> None:
        for relative in ("data/claim_source_links.csv", "data/claim_decision_links.csv"):
            path = self.root / relative
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                fields, rows = list(reader.fieldnames or []), list(reader)
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(row for row in rows if row["claim_id"] != claim_id)

    def test_prototype_only_link_is_acceptable_for_methodological_claim(self):
        self.remove_existing_links("CLM-0002")
        self.add_pev()
        self.add_link(claim_id="CLM-0002")
        self.assertEqual([], self.errors())

    def test_theoretical_claim_cannot_rely_only_on_prototype_link(self):
        self.remove_existing_links("CLM-0001")
        self.add_pev()
        self.add_link(claim_id="CLM-0001")
        self.assert_error_contains("CLM-0001 has no source or decision link")

    def test_novelty_claim_cannot_rely_only_on_prototype_link(self):
        self.remove_existing_links("CLM-0016")
        self.add_pev()
        self.add_link(claim_id="CLM-0016")
        self.assert_error_contains("CLM-0016 has no source or decision link")

    def add_map(self, **overrides: str) -> None:
        row = {
            "map_id": "SCM-9999", "revision_batch": "INFRA-PEV-001",
            "proposal_repository": "example/proposal", "proposal_commit_sha": "b" * 40,
            "proposal_path": "proposal.tex", "section_anchor": "sec:example",
            "claim_id": "CLM-0001", "claim_role": "theoretical_support",
            "traceability_status": "comment_inserted", "last_reviewed": "2026-07-28",
            "notes": "test fixture",
        }
        row.update(overrides)
        self.append("proposal/section_claim_map.csv", row)

    def test_section_map_rejects_unknown_claim(self):
        self.add_map(claim_id="CLM-9999")
        self.assert_error_contains("claim_id references unknown ID 'CLM-9999'")

    def test_comment_inserted_mapping_requires_proposal_commit(self):
        self.add_map(proposal_commit_sha="")
        self.assert_error_contains("comment_inserted mapping lacks proposal_commit_sha")


if __name__ == "__main__":
    unittest.main()
