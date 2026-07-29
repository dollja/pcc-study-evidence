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
EXPECTED_PART_SHA256 = [
    "04ee2efe12bcbcb47d656d24fbadd9f65f0793022ad49c3f5e1704819f679a61",
    "73e9ad49ffb1aa2a508f496aa7a992e01ba12e3c07f01b0470c9729144b9d2ee",
    "d73d3beb1b4de1fdafd2d5c075249a246b3227fdeb602d599ca9f993af97b942",
    "666e20144b300de9431fe9dcb86a6eee2da27861872bcb894995f0da2a5f962b",
    "3c3706eea52731c48397c5185c25415ab6f448493b22adb9f09dc8debf1b6f77",
    "ed1f35c58963d9302335d5f02a27895188dbbca7f7e623cab6118e9c87447ee1",
    "d82b9a1b9bec4f82daad03d14edca7c1fc142a4c5b4fbcfd488c8ca935531940",
    "4b55f2c7f59871da2c8e41f1f70b2255bb5453dd81de55751bbb7f6b3949cfee",
]


class Rev002EvidenceArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parts = sorted(IMPORT_DIR.glob(f"{ARCHIVE_STEM}.b64.v2.part-*"))
        encoded = "".join(path.read_text(encoding="utf-8").strip() for path in cls.parts)
        cls.archive_bytes = base64.b64decode(encoded, validate=True)

    def test_all_canonical_multipart_segments_are_present(self) -> None:
        self.assertEqual(
            [path.name.rsplit("-", 1)[-1] for path in self.parts],
            [f"{index:02d}" for index in range(8)],
        )
        self.assertEqual(
            [hashlib.sha256(path.read_bytes()).hexdigest() for path in self.parts],
            EXPECTED_PART_SHA256,
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
        self.assertTrue(all(name.startswith("evidence/runs/REV-002/") for name in files))
        self.assertIn("evidence/", names)
        self.assertIn("evidence/runs/", names)
        self.assertIn("evidence/runs/REV-002/", names)

    def test_archive_contains_evidence_artifacts_not_prototype_source(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.archive_bytes)) as archive:
            files = [name for name in archive.namelist() if not name.endswith("/")]

        allowed_suffixes = {".md", ".json", ".csv"}
        self.assertTrue(all(PurePosixPath(name).suffix in allowed_suffixes for name in files))
        self.assertFalse(any(PurePosixPath(name).suffix == ".py" for name in files))
        self.assertFalse(any(".." in PurePosixPath(name).parts for name in files))


if __name__ == "__main__":
    unittest.main()
