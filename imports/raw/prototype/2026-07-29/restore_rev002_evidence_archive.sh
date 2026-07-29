#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
NAME="REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4.zip"
OUT_ZIP="${1:-/tmp/${NAME}}"
OUT_DIR="${2:-/tmp/REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4}"

cat "${HERE}/${NAME}.b64.part-"* | base64 --decode > "${OUT_ZIP}"

EXPECTED="$(awk '{print tolower($1)}' "${HERE}/${NAME}.sha256")"
ACTUAL="$(sha256sum "${OUT_ZIP}" | awk '{print $1}')"

if [[ "${ACTUAL}" != "${EXPECTED}" ]]; then
  echo "SHA-256 mismatch" >&2
  echo "expected: ${EXPECTED}" >&2
  echo "actual:   ${ACTUAL}" >&2
  exit 1
fi

unzip -t "${OUT_ZIP}" >/dev/null
rm -rf "${OUT_DIR}"
mkdir -p "${OUT_DIR}"
unzip -q "${OUT_ZIP}" -d "${OUT_DIR}"

printf 'Verified ZIP: %s\n' "${OUT_ZIP}"
printf 'SHA-256: %s\n' "${ACTUAL}"
printf 'Extracted to: %s\n' "${OUT_DIR}"
printf 'Files: %s\n' "$(find "${OUT_DIR}" -type f | wc -l | tr -d ' ')"
