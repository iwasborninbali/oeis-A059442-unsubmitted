# OEIS A059442: Fence conjecture counterexample (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted.** (replaced by the registry tool)
<!-- oeis-status:end -->

## Definition

R(m,n) is the least N such that every red/blue colouring of the edges of K_N contains a red K_m or blue K_n. A059442 lists R(m,n) for m,n>=2 by antidiagonals with offset 0. T(N,k) is the number of partitions of N into exactly k positive parts.

The snapshot `context/A059442.seq` and live [entry](https://oeis.org/A059442), read 2026-11-13, attribute to Jianglin Luo, January 8, 2024: “Fence conjecture: R(m,n) <= (2m-1)*A008284_T(2m-6+n,m) + m + 1  for n >= m >= 3.” The entry still records the conjecture.

## Terms / result

| m | n | T(2m-6+n,m) | proposed upper bound | proved lower bound |
|---:|---:|---:|---:|---:|
| 74 | 74 | 18420969414 | 2707882503933 | 2707882503934 |

The conjecture fails at (74,74), and for all sufficiently large diagonal pairs.

## How it was obtained

An exact partition count gives the claimed upper bound. Erdős's first-moment argument proves a colouring exists on that many vertices with no monochromatic K_74. Partition growth also proves eventual diagonal failure. See [proof.md](proof.md).

## Verification

Two separately written partition recurrences agree, and an independent exact integer inequality proves the first-moment test at 74. The proof is human-checkable, not machine-checked, and no colouring is exhibited. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Luo stated the conjecture; the probabilistic lower bound is due to Erdős (1947). ChatGPT applied it here; Claude Code reviewed the argument. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 programs/producer.py` and `python3 verification/check.py` (both under a second on the recorded machine). The latter prints the partition count, bound, `sufficient integer inequality: True` and `PASS`. Full output is in `verification/logs/`.

## Provenance

Source `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`, paths `tasks/2026-11-12-A059442-ramsey-fence/answers/2026-11-12-chatgpt.md`, `context/A059442.seq`, and `TASK.md`. Guide review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
