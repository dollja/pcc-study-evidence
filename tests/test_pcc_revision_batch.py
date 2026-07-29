import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts import pcc_revision_batch as revision


ROOT = Path(__file__).resolve().parents[1]


class RevisionBatchTests(unittest.TestCase):
    def setUp(self):
        self.manifest = revision.load_manifest(ROOT / "workflow/batches/REV-002.json")

    def test_rejects_malformed_shas(self):
        with tempfile.TemporaryDirectory() as directory:
            malformed = copy.deepcopy(self.manifest)
            malformed["repositories"]["prototype"]["merge_sha"] = "abc123"
            path = Path(directory) / "batch.json"
            path.write_text(json.dumps(malformed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "40-character lowercase SHA"):
                revision.load_manifest(path)

    def test_future_merges_render_explicit_unresolved_markers(self):
        rendered = revision.render_launcher(self.manifest, "prompt_c")
        self.assertIn(revision.UNRESOLVED, rendered)

    def test_collects_prototype_manifests_from_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "run").mkdir()
            (root / "run/benchmark.manifest.json").write_text(
                json.dumps({"commit_sha": "a" * 40}), encoding="utf-8"
            )
            self.assertEqual(
                revision.collect_prototype_manifests(root),
                [{"path": "run/benchmark.manifest.json", "manifest": {"commit_sha": "a" * 40}}],
            )

    def test_preserves_noncanonical_evidence_exclusion(self):
        rendered = revision.render_launcher(self.manifest, "closure")
        self.assertIn("not canonical reproduced PEV evidence", rendered)
        self.assertIn("does not provide novelty proof", rendered)

    def test_renders_all_launchers_with_recorded_merge_shas(self):
        manifest = copy.deepcopy(self.manifest)
        for index, repository in enumerate(manifest["repositories"].values(), start=1):
            repository["merge_sha"] = str(index) * 40
        with tempfile.TemporaryDirectory() as directory:
            paths = revision.render_all(manifest, directory)
            self.assertEqual([path.name for path in paths], [
                "prompt_c_launcher.md", "prompt_d_launcher.md", "closure_launcher.md"
            ])
            combined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
            for index in range(1, 4):
                self.assertIn(str(index) * 40, combined)
            self.assertNotIn(revision.UNRESOLVED, combined)


if __name__ == "__main__":
    unittest.main()
