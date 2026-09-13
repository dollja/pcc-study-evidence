"""Validate author-decision metadata, not corpus quality or research findings."""
import csv
import hashlib
import json
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "studies/episode_history/ai_authored_candidates"


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


class CandidateAuthorAcceptanceMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current = rows(DATA / "acceptance_review_register.csv")
        cls.original = rows(DATA / "history/acceptance_review_register.v0.1.0.csv")
        cls.manifest = json.loads((DATA / "manifest.json").read_text())

    def test_exact_episode_inventory(self):
        expected = [f"E{i:03}" for i in range(1, 31)]
        self.assertEqual([r["episode_id"] for r in self.current], expected)
        self.assertEqual(self.manifest["episode_ids"], expected)
        self.assertEqual(self.manifest["episode_count"], len(expected))

    def test_original_independent_review_columns_preserved(self):
        self.assertEqual(len(self.original), len(self.current))
        for old, new in zip(self.original, self.current):
            self.assertEqual(old, {key: new[key] for key in old})

    def test_author_acceptance_is_instruction_based(self):
        for row in self.current:
            self.assertEqual(row["author_acceptance"], "Accept")
            self.assertEqual(row["author_reviewer_id"], "author_review")
            self.assertEqual(row["author_decision_id"], "DEC-0025")
            self.assertIn("Author instructed", row["author_reason"])
            self.assertIn("no independent-review rationale supplied", row["author_reason"])

    def test_date_and_unchanged_episode_versions(self):
        for row in self.current:
            self.assertEqual(row["episode_version"], "0.1.0")
            self.assertEqual(date.fromisoformat(row["author_decision_date"]), date(2026, 9, 13))
        self.assertEqual(self.manifest["registration_version"], "0.1.1")
        self.assertFalse(self.manifest["episode_and_rule_bytes_changed"])

    def test_independent_reviews_still_pending(self):
        for row in self.current:
            for field in ("task_coherence_review", "independent_rule_review", "source_sensitivity_review", "human_acceptance"):
                self.assertEqual(row[field], "pending")
            for field in ("reviewer_id", "review_date", "decision", "revision_required", "notes"):
                self.assertEqual(row[field], "")
        for field in ("independent_material_acceptance", "independent_rule_review", "privacy_release_review"):
            self.assertEqual(self.manifest[field], "pending")

    def test_register_digests(self):
        for path, key in (
            (DATA / "acceptance_review_register.csv", "current_acceptance_register_sha256"),
            (DATA / "history/acceptance_review_register.v0.1.0.csv", "original_acceptance_register_sha256"),
        ):
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), self.manifest[key])
        for key in ("source_package_sha256", "source_corpus_manifest_sha256"):
            self.assertRegex(self.manifest[key], r"^[0-9a-f]{64}$")

    def test_no_scientific_or_release_status_promotion(self):
        for field in ("independent_human_authors", "reference_annotation_records", "model_prediction_records", "benchmark_evaluations"):
            self.assertEqual(self.manifest[field], 0)
        self.assertEqual(self.manifest["evidence_status_changes"], [])
        self.assertFalse(self.manifest["public_corpus_release_authorized"])
        self.assertEqual(self.manifest["participant_use_authorization"], "not_established_by_this_record")
        self.assertIsNone(self.manifest["corpus_storage_locator"])

    def test_study_sets_remain_separate(self):
        self.assertEqual(set(self.manifest["no_automatic_inclusion_in"]), {
            "ACS construction", "actor-state construction", "development example",
            "independently human-authored pilot", "main evaluation"})
        self.assertEqual(self.manifest["study_inclusion"], "unassigned_AI_authored_candidate_stratum")
        self.assertEqual(self.manifest["task_structure_counts"], {
            "scheduling": 10, "release_authorization": 10, "completion_handoff": 10})

    def test_metadata_only_directory(self):
        files = {str(p.relative_to(DATA)) for p in DATA.rglob("*") if p.is_file()}
        self.assertEqual(files, {"README.md", "manifest.json", "author_decision_20260913.md",
                                "acceptance_review_register.csv", "history/acceptance_review_register.v0.1.0.csv"})
        self.assertFalse(self.manifest["corpus_payload_included"])
        self.assertFalse(self.manifest["restricted_source_material_included"])

    def test_decision_register_link(self):
        matches = [r for r in rows(ROOT / "data/decisions.csv") if r["decision_id"] == "DEC-0025"]
        self.assertEqual(len(matches), 1)
        record = matches[0]
        self.assertEqual(record["participants"], "author_review")
        self.assertEqual(record["authority_level"], "author_confirmed")
        self.assertIn("candidate material only", record["decision"])
        self.assertIn("remain pending", record["rationale"])
        self.assertEqual(record["affected_claims"], "")


if __name__ == "__main__":
    unittest.main()
