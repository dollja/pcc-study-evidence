from __future__ import annotations

import base64
import hashlib
import io
import unittest
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
IMPORT_DIR = ROOT / "imports" / "raw" / "prototype" / "2026-07-29"
ARCHIVE_STEM = "REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4.zip"
EXPECTED_SHA256 = "b13361c994ba522595f97a654e53ef08fb4bd66c7982503664fe14dd048f8d6c"


class Rev002EvidenceArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parts = sorted(IMPORT_DIR.glob(f"{ARCHIVE_STEM}.b64.part-*"))
        encoded = "".join(path.read_text(encoding="utf-8").strip() for path in cls.parts)
        cls.archive_bytes = base64.b64decode(encoded, validate=True)

    def test_all_multipart_segments_are_present(self) -> None:
        self.assertEqual(
            [path.name.rsplit("-", 1)[-1] for path in self.parts],
            [f"{index:02d}" for index in range(8)],
        )

    def test_decoded_archive_matches_supplied_checksum(self) -> None:
        digest = hashlib.sha256(self.archive_bytes).hexdigest()
        self.assertEqual(digest, EXPECTED_SHA256)

        checksum_file = IMPORT_DIR / f"{ARCHIVE_STEM}.sha256"
        recorded = checksum_file.read_text(encoding="utf-8").split()[0].lower()
        self.assertEqual(recorded, EXPECTED_SHA256)

    def test_archive_is_valid_and_contains_expected_evidence_tree(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.archive_bytes)) as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            files = [name for name in names if not name.endswith("/")]

        self.assertEqual(len(names), 65)
        self.assertEqual(len(files), 47)
        self.assertIn("evidence/runs/REV-002/README.md", files)
        self.assertTrue(all(name.startswith("evidence/runs/REV-002/") for name in names))

    def test_archive_contains_evidence_artifacts_not_prototype_source(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.archive_bytes)) as archive:
            files = [name for name in archive.namelist() if not name.endswith("/")]

        allowed_suffixes = {".md", ".json", ".csv"}
        self.assertTrue(all(PurePosixPath(name).suffix in allowed_suffixes for name in files))
        self.assertFalse(any(PurePosixPath(name).suffix == ".py" for name in files))
        self.assertFalse(any(".." in PurePosixPath(name).parts for name in files))


if __name__ == "__main__":
    unittest.main()
