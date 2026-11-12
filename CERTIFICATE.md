# Verification certificate

## Claim

R(74,74)>2707882503933, the proposed upper bound at (74,74).

The proposed upper bound fails for every sufficiently large diagonal pair.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Human-checkable proof | `proof.md` | Adapted by OpenAI Codex from ChatGPT, 2026-11-12 | First-moment argument and eventual failure | Not machine-checked |
| Producer | `programs/producer.py` | ChatGPT, 2026-11-12 | Two partition counts, exact criteria through 200 | Passed |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | Partition recurrence and stronger exact inequality at 74 | Passed |

The programs share mathematical constants but no code or data. The independent check uses a different recurrence and a sufficient inequality. Guide review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/producer.py` and `python3 verification/check.py` passed. The latter prints `T(216,74): 18420969414`, `fence bound: 2707882503933`, `sufficient integer inequality: True`, `PASS`. Full logs are in `verification/logs/`.

## Not covered

No explicit colouring is constructed. The all-large-indices proof uses the classical Erdős lower bound and is not formally machine-checked. The independent check does not recheck the producer's entire scan or its reported known Ramsey values.

## Guide's independent check

pending

## Verdict

complete — the exact counterexample check was independently replayed in full; the accompanying proofs remain human-checkable, not machine-checked.
