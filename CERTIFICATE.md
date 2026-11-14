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
| Independent referee and check | `verification/agent-2026-11-15/` (REPORT.md, independent_check.py) | ChatGPT agent, 2026-11-15; own code, no repository code | T(216,74), B, the exact inequality 2B^74 < 74! 2^2701, and the diagonal indices 74..1200; proof read line by line | Passed; proof correct, minor exposition gaps |

The programs share mathematical constants but no code or data. The independent check uses a different recurrence and a sufficient inequality. Guide review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/producer.py` and `python3 verification/check.py` passed. The latter prints `T(216,74): 18420969414`, `fence bound: 2707882503933`, `sufficient integer inequality: True`, `PASS`. Full logs are in `verification/logs/`.

2026-11-15, Darwin arm64, Python 3.14.6, by the guide: `python3 independent_check.py` in `verification/agent-2026-11-15/`
finished in 12.7 s with `PASS` (passing diagonal indices 74..1200, 1127 of them).

## Not covered

No explicit colouring is constructed. The all-large-indices proof uses the classical Erdős lower bound and is not formally machine-checked. The independent check does not recheck the producer's entire scan or its reported known Ramsey values.

## Guide's independent check

15 November 2026: the guide read `proof.md` line by line. At m = n = 74 the fence bound is 147 T(216,74) + 75 =
2,707,882,503,933 (147 x 18,420,969,414 + 75 checked by hand). The first-moment argument needs 2 C(B,74) < 2^2701; in
bits, 74 log2 B + 1 = 3057.2 against log2 74! + 2701 = 3058.2, a margin of about one bit, so the exact integer check is
essential (it passes in the referee's and the repository's programs). For large k, T(3k-6,k) <= p(2k-6) and
log p(s) <= ts + pi^2/(6t) (Euler product, e^x - 1 >= x), so the fence bound is exp(O(sqrt k)), below Erdos's 2^(k/2).
Verdict: correct.

## Verdict

complete — R(74,74) > 2,707,882,503,933 and the eventual failure of the fence bound are proved (read independently
by the guide and by a separate referee); the exact inequality is checked by two programs that share no code.
Not covered: no formal proof; no explicit colouring is produced (the argument is probabilistic).
