# REV-002 post-merge corrections

Evidence PR #8 was merged to `main` as
`39e8df1f5a6d414fc492ef1abc973b45604d50f2`; its branch-head SHA was
`8c9b59f7e2e0f9f6d1099614fba7bb3f47ace613`.

Post-merge review found that PEV-0015 had acquired a second-order chronology
limitation that is not present in its retained result artifact. PEV-0015 now
records only the seven limitations present in that artifact. The chronology
limitation remains preserved by PEV-0010 as `recorded_unverified`.

CPE-0032 was withdrawn following post-merge review because PEV-0015 does not
test or implement the detection-only or no-autonomous-repair boundary in
CLM-0026. Stable ID CPE-0032 is retired and must never be reassigned. No
replacement claim-prototype link is asserted. A future link requires a
retained artifact that directly exercises the relevant boundary.
