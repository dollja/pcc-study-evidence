#!/usr/bin/env python3
"""Validate and render cross-repository PCC revision-batch manifests."""

import argparse
import json
import re
from pathlib import Path


SHA_RE = re.compile(r"^[0-9a-f]{40}$")
UNRESOLVED = "UNRESOLVED—record only after the corresponding PR is reviewed and merged"
STAGES = ("prompt_c", "prompt_d", "closure")


def load_manifest(path):
    """Load *path* and validate the revision-control fields used by launchers."""
    path = Path(path)
    with path.open(encoding="utf-8") as stream:
        manifest = json.load(stream)
    if not re.fullmatch(r"REV-\d{3}", manifest.get("batch_id", "")):
        raise ValueError("batch_id must have the form REV-###")
    for name, repository in manifest.get("repositories", {}).items():
        for field in ("baseline_sha", "merge_sha"):
            value = repository.get(field)
            if value is not None and not SHA_RE.fullmatch(value):
                raise ValueError(f"{name}.{field} must be null or a 40-character lowercase SHA")
    missing = set(STAGES) - set(manifest.get("stages", {}))
    if missing:
        raise ValueError("missing stages: " + ", ".join(sorted(missing)))
    return manifest


def collect_prototype_manifests(root):
    """Return parsed prototype manifest files below *root*, in stable order."""
    root = Path(root)
    result = []
    for path in sorted(root.rglob("*.json")):
        if path.name.endswith("manifest.json") or path.name == "manifest.json":
            with path.open(encoding="utf-8") as stream:
                result.append({"path": str(path.relative_to(root)), "manifest": json.load(stream)})
    return result


def resolved_sha(repository):
    """Render a merge SHA without guessing a future value."""
    return repository.get("merge_sha") or UNRESOLVED


def render_launcher(manifest, stage):
    """Render one launcher from canonical manifest state."""
    if stage not in STAGES:
        raise ValueError(f"unknown stage: {stage}")
    lines = [
        f"# {manifest['batch_id']} — {manifest['stages'][stage]['title']}",
        "",
        "> Derived launcher. The batch manifest—not conversation history or this prompt—is",
        "> authoritative for SHAs and stage state.",
        "",
        f"Stage state: `{manifest['stages'][stage]['state']}`",
        "",
        "## Recorded repository revisions",
        "",
    ]
    for name, repository in manifest["repositories"].items():
        lines.append(f"- `{name}` merge SHA: `{resolved_sha(repository)}`")
    lines.extend([
        "",
        "Future merge SHAs may be recorded only after the corresponding PR has been reviewed and merged.",
        "",
        "## Evidence boundary",
        "",
        f"`{manifest['remediation_baseline']}` is a remediation baseline and audit trail,",
        "not canonical reproduced PEV evidence. It is excluded from canonical PEV findings",
        "and does not provide novelty proof.",
        "",
    ])
    return "\n".join(lines)


def render_all(manifest, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for stage in STAGES:
        path = output_dir / f"{stage}_launcher.md"
        path.write_text(render_launcher(manifest, stage), encoding="utf-8")
        written.append(path)
    return written


def default_output(manifest_path, manifest):
    return Path(manifest_path).resolve().parents[2] / "generated" / manifest["batch_id"]


def main(argv=None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("status", "render"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--manifest", required=True)
        if command == "render":
            subparser.add_argument("--output-dir")
    args = parser.parse_args(argv)
    try:
        manifest = load_manifest(args.manifest)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    if args.command == "status":
        print(f"{manifest['batch_id']}: {manifest['status']}")
        for stage in STAGES:
            print(f"{stage}: {manifest['stages'][stage]['state']}")
        for name, repository in manifest["repositories"].items():
            print(f"{name}: {resolved_sha(repository)}")
    else:
        output_dir = args.output_dir or default_output(args.manifest, manifest)
        for path in render_all(manifest, output_dir):
            print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
