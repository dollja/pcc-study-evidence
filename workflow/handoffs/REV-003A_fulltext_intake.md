# REV-003A exact full-text intake handoff

## Scope

This operation stages exact full-text inputs for `SRC-0002`, `SRC-0003`, and `SRC-0010`. It does not perform the thirteen-field mechanism audit and does not change `NOV-0001`.

## Source controls

- **SRC-0002** - *Commitments, Beliefs and Intentions in Dialogue*; path `imports/raw/literature/REV-003A/SRC-0002_asher_lascarides_2008_londial.pdf`; SHA-256 `b1ee3b83b64d498f04306c7618d4ab789ea89c78f7eb3595037412cf82b3e3e4`; size `183452` bytes; Author-hosted copy of LONDIAL 2008 proceedings paper; 8 PDF pages.
- **SRC-0003** - *Dynamics of Public Commitments in Dialogue*; path `imports/raw/literature/REV-003A/SRC-0003_venant_asher_2015_iwcs.pdf`; SHA-256 `3aa59f34f28d3c0b1f657f84a754bc3253e24eb10bf9de136eb06944e5df75e3`; size `190360` bytes; ACL Anthology W15-0131; IWCS 2015; 11 PDF pages.
- **SRC-0010** - *Common Ground Tracking in Multimodal Dialogue*; path `imports/raw/literature/REV-003A/SRC-0010_khebour_et_al_2024_lrec_coling.pdf`; SHA-256 `0c6fb58d3310a34f95af014b64f331a74556e74d5736892fc252e0da4943ae4d`; size `2748388` bytes; ACL Anthology 2024.lrec-main.318; LREC-COLING 2024; 16 PDF pages.

## Next authorized operation

After this intake PR is reviewed and merged, run the REV-003A exact full-text mechanism audit. Create source cards for `SRC-0002`, `SRC-0003`, and `SRC-0010`, update only locator-backed registers, retain `NOV-0001` as `candidate`, and do not begin Prompt C until the combined Tier 1 synthesis is reviewed.
