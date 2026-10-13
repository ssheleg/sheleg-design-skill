# FW05 ledger correction — 2026-10-13

The aggregate umbrella check found the newest verification heading still at
1.64.1 after accepted publication of 1.64.2. Both the original implementation and
packaging review missed this documentation propagation. This change adds a new
1.64.2 section tied to the existing source, release and registry receipts; it
preserves historical observations and does not upgrade runtime claims.

Baseline: the same heading extraction used by umbrella
`check_each_member_ledger_reaches_its_shipped_version` returned 1.64.1 while
`package.json` returned 1.64.2. After correction both return 1.64.2. No ratchet
floor or umbrella guard changed.

`npm pack --dry-run --json` enumerated exactly the 1238 paths in the immutable
[registry receipt](https://github.com/ssheleg/sshlg-skills/blob/e3b8f4213a1c807af6708a85339d0a8f87081544/docs/evidence/completion-1013/releases/design-1.64.2.json).
Every local file length and SHA-256 equals its recorded registry value. This proves
payload parity; it does not claim the tarball container bytes are identical.
Only excluded `docs/` files change. Keep version and annotated tag 1.64.2.

Local `python3 test/validate.py`: exit 0, 6654 checks. `git diff --check`: exit 0.
A new full local suite was not run for these excluded documentation changes;
genuine candidate CI remains the integration gate.

Next: independent review, frozen deliberate candidate promotion, genuine required
checks and normal merge. Then the umbrella may pin this documentation successor
without claiming a new package release. Native/browser/provider acceptance is
unchanged and unobserved by this correction.
