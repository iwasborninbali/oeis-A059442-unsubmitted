# Independent verification report — 2026-11-15

Repository: `iwasborninbali/oeis-A059442-unsubmitted`, input commit
`1e97784a7175ddd61d0a3582f795f888c20ba822`. Independent referee:
ChatGPT (not a contributor to the original repository material). The uploaded
archive was unpacked and `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`,
`proof.md`, `programs/producer.py`, `verification/check.py`, and the two
existing verification logs were read before starting the independent check.

## Claim

**Exactly as asserted in `CERTIFICATE.md`:**
`R(74,74) > 2707882503933` (the proposed Fence upper bound at `(74,74)`),
and that proposed upper bound fails at every sufficiently large diagonal pair.

These are existence/lower-bound assertions, not an explicit graph-coloring
construction. The certificate does **not** claim that 74 is the smallest
actual counterexample, that off-diagonal pairs have been analyzed, or that a
formal proof assistant has checked the argument.

## Proof check

**Referee verdict on `proof.md`: correct (minor, fixable exposition omissions;
no fatal gaps or reliance on an unproved conjecture).** Line-numbered audit:

- **Line 3:** `T(N,k)=T(N-1,k-1)+T(N-k,k)` is correct: partition into those
  having a part 1 and those whose every part is at least 2. Its base cases
  suffice for nonnegative arguments reached during the calculation. The
  formula `B=147*T(216,74)+75`, count, and numerical bound are correct.
  **No gap.** The claimed integer values require a computational check;
  checked independently below.
- **Line 5, first two sentences:** A fixed 74-set is monochromatic with
  probability `2^(1-C(74,2))`; there are `C(B,74)` such sets, so the
  expectation is `2*C(B,74)/2^2701`. **No gap.** (The proof explicitly
  says that the edge colors are independent and equiprobable.)
- **Line 5, exact integer certificate:**
  `2*B^74 < 74!*2^2701` is correct. It is asserted on the basis of code,
  rather than accompanied by the enormous integers in the written proof.
  **Fixable presentation/evidence dependency, not a mathematical defect:**
  independently re-evaluate exact integer arithmetic; the new program
  checks both this sufficient test and the sharper direct binomial test.
- **Line 5, final inference:** `C(B,74) <= B^74/74!`; expectation `<1`
  forces at least one outcome having no monochromatic 74-clique, hence
  `R(74,74)>B`. **No gap, no explicit coloring needed.**
- **Line 7:** Subtracting 1 from each of 74 (or `k`) positive parts gives
  a partition of `2k-6` with at most `k` positive parts, and conversely
  zero-padding and adding 1 reverses the bijection. **No gap.**
- **Lines 7-10:** The claimed upper bound for unrestricted partitions
  follows from Euler's generating product. **One fixable omitted
  intermediate step:** for `s>=1,t>0`,
  `p(s)*exp(-ts) <= P(exp(-t)) = product_{r>=1}(1-exp(-tr))^(-1)`;
  then `log P(exp(-t)) = sum_{j>=1} 1/(j*(exp(t*j)-1))`
  and `exp(x)-1 >= x` yield `log p(s) <= ts+pi^2/(6t)`.
  Everything is valid. No unproved hypothesis is used.
- **Line 12, partition growth:** Taking `t=s^(-1/2)` proves
  `log p(s) <= (1+pi^2/6)*sqrt(s)`; multiplication by `2k-1` and addition
  of `k+1` leave the proposed bound with logarithm `O(sqrt(k)+log k)`.
  **No gap.**
- **Line 12, Ramsey lower bound:** The established Erdős (1947) theorem
  `R(k,k)>2^(k/2)` is accurately invoked. **No conjectural dependency.**
  A full citation or derivation from the same first-moment inequality would
  improve self-containment but is not needed for validity.
- **Line 12, asymptotic comparison:** `O(sqrt(k)+log k)=o(k)`, while
  `(k/2)*log 2` is linear. Thus the Ramsey number eventually exceeds the
  proposed bound. **No gap.**

All mathematical steps are valid. The two omissions are expository and
fixable, not counterexamples to the proof. There is **no fatal gap**.

**Optional independent strengthening (proves failure for *every* k>=74):**
The exact scan certifies every `74<=k<=255` individually. For all `k>=256`,
Euler's estimate and `1+pi^2/6<3` give
`B_k <= 3k*exp(3*sqrt(2k))` (because `T(3k-6,k)<=p(2k-6)`).
Set `h(x)=x/3-3*sqrt(2x)-log(3x)`; then `h(256)>0` (indeed
`3*sqrt(512)<69`, `log(768)<7`, while `256/3>85`), and
`h'(x)=1/3-3/sqrt(2x)-1/x>0` for every `x>=256`.
Since `log(2)>2/3`, for these k,
`B_k < exp(k/3) < 2^(k/2) < R(k,k)`.
Consequently the revised upper bound fails for **every diagonal k>=74**,
not merely for unspecified sufficiently large k. This does **not** establish
that 74 is the first genuine failure: the first-moment test is only sufficient.

## Independent computation

Independent source: `independent_check.py`; complete output:
`independent_check.log`. No repository code or data is imported. Python 3.13.5.

**Method:** Generate unrestricted integer partition counts `p(0)..p(2394)`
with Euler's generalized pentagonal-number recurrence. For `q=n-k <2(k+1)`,
subtract from `p(q)` the partitions with a part greater than `k`. Such a
partition has exactly one oversized part, hence
`T(n,k) = p(q) - sum_{r=0}^{q-k-1}p(r)` (empty sum is zero).
At diagonal `(k,k)`, `n=3k-6`, `q=2k-6` always satisfies this condition.
This differs from both original restricted-partition recurrences.

For **every integer k=3..1200 inclusive**, evaluate the exact first-moment
comparison `2*binomial(B(k,k),k) < 2^binomial(k,2)` using big integers.
No floating-point decision procedure is used.

- **At 74:** `T(216,74)=18420969414`;
  `B(74,74)=2707882503933`; `2*binomial(B,74)<2^2701` is **true**.
  The stronger `2*B^74 < 74!*2^2701` is **true**, with left/right
  bit lengths **3058/3059**. `floor(10^12*E)=517687461224`, so
  the expected number is approximately **0.517687461224...**.
- **At 96:** `T(282,96)=1171023653997`, `B(96,96)=223665517913524`.
- **Full exact scan:** test is false for every `3<=k<=73`, and true for
  **every `74<=k<=1200`** (1127 consecutive successes, no exceptions).
  This is six times the range of the original producer scan `3..200` and
  greatly exceeds the independent certificate's single-index check.
- **Nine recorded small exact Ramsey values:** All nine proposed-bound
  checks agree with the recorded known values (9/9 pass). Those nine
  known Ramsey values were *used as inputs*, not independently proved.
- **Runtime:** Python `perf_counter()` elapsed **2.233 s**;
  external `/usr/bin/time` **3.22 CPU user seconds**, **0.27 CPU system
  seconds**, **3.09 wall seconds** in the available container.

SHA-256 (raw local UTF-8 files):

| File | SHA-256 |
|---|---|
| `independent_check.py` | `becbd5c36ee8a9044fc1ebc8c442e02e43217490f19fdc15bce5f663105b30ab` |
| `independent_check.log` | `6d0eb74cea12820f138c7517fb568f1d10f9e2dca8c40ec37f47400b4700ae44` |

## Prior art

Search performed on **2026-11-15**. This is a targeted public-source search,
not a guarantee of global publication priority.

1. **The live OEIS A059442** still contains Jianglin Luo's exact revised
   inequality, attributed in its comment to **2024-01-08**:
   https://oeis.org/A059442 . Its **history** link
   https://oeis.org/history?seq=A059442 returned **HTTP 403**, so individual
   OEIS revision records could not be inspected; the date in the public
   comment and the earlier dated MSE post below are directly visible.
2. **Previously missing direct prior art:** Cody/Jianglin Luo posted the
   *Fence Conjecture* on Mathematics Stack Exchange on **2023-11-22** and
   **revised it on 2023-12-02** to the exact OEIS upper-bound inequality:
   https://math.stackexchange.com/questions/4812195/ . Misha Lavrov's
   **2023-11-27** answer refutes Luo's **original proposed equality**
   using the known asymptotic `R(3,n)=O(n^2/log n)`, whereas the proposed
   equality would be quadratic. This does **not**, by itself, refute
   Luo's later **weaker upper bound**. The repository's `PRIOR-ART.md`
   omitted this highly relevant discussion.
3. **Erdős, 1947**, *Some remarks on the theory of graphs*,
   *Bulletin of the American Mathematical Society* 53, 292-294,
   https://doi.org/10.1090/S0002-9904-1947-08785-X , already proves the
   probabilistic Ramsey lower bound. Its exact first-moment criterion
   is reproduced in Yufei Zhao's lecture notes (Theorem 1.1.2):
   https://yufeizhao.com/pm/fa20/probmethod_notes.pdf . This **is not a
   new probabilistic method**.
4. **OEIS cross-references** checked:
   https://oeis.org/A212954 (alternate Ramsey table),
   https://oeis.org/A000791 (the exact small `R(3,n)` values),
   https://oeis.org/A120414 (a **different** diagonal Ramsey proposal),
   https://oeis.org/A008284 (partition triangle),
   https://oeis.org/A000070 (cumulative partitions).
   In fact, A008284's comment attributed to **Richard R. Forberg,
   2014-12-26** already states a formula equivalent to this verifier's
   `p(q)-sum p(r)` subtraction in the needed domain. The partition
   identity is also **not new**.
5. **arXiv:** searches for `"Fence conjecture" Ramsey`, `"A059442"`,
   `"Jianglin Luo" Ramsey partitions`, and the exact bound expression
   found no arXiv paper explicitly proving/refuting the revised fence
   inequality. Relevant general literature includes Campos, Griffiths,
   Morris, Sahasrabudhe, *An exponential improvement for diagonal Ramsey*,
   arXiv:2303.09521 (2023), https://arxiv.org/abs/2303.09521 ; its
   subject is general diagonal upper bounds, not this conjecture.
6. **MathOverflow:** targeted site searches for `"Fence conjecture"
   Ramsey`, `"A059442"`, and `Luo Ramsey partition` found no discussion
   of this precise revised bound.
7. **zbMATH Open:** targeted indexed searches for `"Fence conjecture"
   Ramsey` and `"A059442"` yielded no matching mathematical publication;
   direct zbMATH query access was unavailable in this environment.
   **Absence cannot be certified from a blocked search interface.**
8. **Journals:** targeted searches of AMS, *Electronic Journal of
   Combinatorics*, Springer, Elsevier/ScienceDirect, and other indexed
   combinatorics literature found the classical Erdős Ramsey bound and
   classical partition estimates but no prior journal proof or
   counterexample for this particular revised Fence bound. Search terms
   included `"Fence conjecture" Ramsey`, `"2m-1" "A008284" Ramsey`,
   `"2707882503933" Ramsey`, `"18420969414" Ramsey`.

**Novelty assessment:** The precise explicit counterexample `(74,74)` and
its all-large diagonal application were **not located in these searches**,
but an exhaustive priority assertion is **not established**. The underlying
probabilistic argument and the partition-counting mathematics predate the
repository by decades. The public 2023 MSE discussion is essential prior
art; the general subexponential-vs-exponential contradiction follows
immediately from known results, even if its application to Luo's revised
statement has not been found published elsewhere.

## Verdict

**COMPLETE mathematical verification.** Both parts of the certificate's
claim are true, the exact integer certificate was independently recomputed,
the larger scan passed, the asymptotic argument is valid, and the only
identified gaps are fixable exposition omissions. Additionally, exact
checks through 255 and the analytic comparison for all `k>=256` jointly
establish failure of the proposed bound for every diagonal `k>=74`.
No explicit coloring, proof of the nine small historical Ramsey values,
formal proof-assistant certificate, or proof of **first genuine failure at
74** is claimed or needed.

**Novelty/priority: NOT ESTABLISHED.** No precise earlier revised-bound
counterexample was found, but the technique is classical, Luo's earlier
2023 MSE discussion must be credited, and the search was not exhaustive.
