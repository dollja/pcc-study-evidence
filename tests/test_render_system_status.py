import json
import tempfile
import unittest
from pathlib import Path

from scripts import render_system_status as status


ROOT = Path(__file__).resolve().parents[1]


class SystemStatusTests(unittest.TestCase):
    def fixture(self, directory: str) -> Path:
        root = Path(directory)
        (root / "workflow/batches").mkdir(parents=True)
        (root / "workflow/handoffs").mkdir()
        (root / "imports/raw/literature/REV-003A").mkdir(parents=True)
        manifest = json.loads((ROOT / "workflow/batches/REV-003.json").read_text())
        (root / "workflow/ACTIVE_BATCH").write_text("REV-003\n", encoding="utf-8")
        (root / "workflow/batches/REV-003.json").write_text(json.dumps(manifest), encoding="utf-8")
        required_paths = {manifest["latest_handoff"], *manifest["next_task"]["authorization_files"]}
        for relative_path in required_paths:
            path = root / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("fixture\n", encoding="utf-8")
        return root

    def test_active_batch_resolution(self):
        batch_id, path = status.resolve_active_batch(ROOT)
        self.assertEqual("REV-003", batch_id)
        self.assertEqual(ROOT / "workflow/batches/REV-003.json", path)

    def test_rendering_is_deterministic(self):
        manifest = status.load_state(ROOT)
        self.assertEqual(status.render_status(manifest), status.render_status(manifest))

    def test_malformed_sha_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            path = root / "workflow/batches/REV-003.json"
            manifest = json.loads(path.read_text())
            manifest["operations"]["source_intake"]["merge_sha"] = "abc123"
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "40-character SHA"):
                status.load_state(root)

    def test_missing_handoff_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            path = root / "workflow/batches/REV-003.json"
            manifest = json.loads(path.read_text())
            (root / manifest["latest_handoff"]).unlink()
            with self.assertRaisesRegex(FileNotFoundError, "latest handoff"):
                status.load_state(root)

    def test_missing_next_task_authorization_file_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            path = root / "workflow/batches/REV-003.json"
            manifest = json.loads(path.read_text())
            relative_path = next(
                item
                for item in manifest["next_task"]["authorization_files"]
                if item != manifest["latest_handoff"]
            )
            (root / relative_path).unlink()
            with self.assertRaisesRegex(FileNotFoundError, "next-task authorization file"):
                status.load_state(root)

    def test_source_intake_is_distinct_from_completed_audit(self):
        rendered = status.render_status(status.load_state(ROOT))
        self.assertIn("Source intake and substantive mechanism audit are distinct operations", rendered)
        self.assertIn("REV-003B full-text mechanism audit", rendered)
        self.assertIn("SRC-0004 exact full-text mechanism audit", rendered)

    def test_exact_src0004_access_gap_is_resolved(self):
        rendered = status.render_status(status.load_state(ROOT))
        self.assertIn("`SRC-0004`", rendered)
        self.assertIn("**Exact-source access gaps:** None recorded.", rendered)

    def test_finalization_is_blocked_on_author_confirmations(self):
        rendered = status.render_status(status.load_state(ROOT))
        self.assertIn("**Batch status:** `evidence_finalization_blocked_on_author_confirmations`", rendered)
        self.assertIn("**Last completed operation:** REV-003A exact full-text mechanism audit and combined Tier 1 synthesis", rendered)
        self.assertIn("**Task:** REV-003 author confirmations for evidence finalization", rendered)
        self.assertIn("**Task state:** `blocked`", rendered)
        self.assertIn("**Current work state:** `blocked`", rendered)
        self.assertIn("downstream work is not authorized", rendered)
        self.assertIn("## Downstream stage gates", rendered)
        self.assertIn("**Prompt C downstream gate:** `blocked_on_author_confirmations`", rendered)
        self.assertIn("workflow/handoffs/REV-003_evidence_finalization.md", rendered)

    def test_nov0001_remains_candidate(self):
        rendered = status.render_status(status.load_state(ROOT))
        self.assertIn("NOV-0001 remains candidate", rendered)


if __name__ == "__main__":
    unittest.main()
