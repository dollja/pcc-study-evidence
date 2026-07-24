from __future__ import annotations

import unittest

from scripts.validate_registers import validate_all, validate_novelty_wording


class RegisterValidationTests(unittest.TestCase):
    def test_repository_registers_validate(self):
        errors, counts = validate_all()
        self.assertEqual([], errors, "\n".join(errors))
        self.assertGreaterEqual(counts.get("data/sources.csv", 0), 30)
        self.assertGreaterEqual(counts.get("data/claims.csv", 0), 20)

    def test_strong_novelty_wording_is_rejected_for_candidate(self):
        errors = validate_novelty_wording({
            "novelty_id": "NOV-9999",
            "audit_status": "candidate",
            "current_wording": "This is the first system to solve the problem.",
        })
        self.assertTrue(errors)

    def test_cautious_candidate_wording_is_allowed(self):
        errors = validate_novelty_wording({
            "novelty_id": "NOV-9999",
            "audit_status": "candidate",
            "current_wording": "This is a proposed combination and evaluation target.",
        })
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
