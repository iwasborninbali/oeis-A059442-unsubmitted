# Proof

Let T(N,k) count partitions of N into exactly k positive parts, and let R(m,n) be the least number of vertices forcing a red K_m or blue K_n in every two-colouring. At m=n=74 the proposed fence bound is B=147 T(216,74)+75. The independent checker uses T(N,k)=T(N-1,k-1)+T(N-k,k), with T(0,0)=1 and T(N,k)=0 when k<=0<N or k>N. The first term counts partitions containing a 1 after deleting it; the second counts partitions all of whose k parts are at least 2 after subtracting 1 from each. It finds T(216,74)=18420969414 and B=2707882503933.

Colour each edge of K_B independently red or blue with equal probability. Each fixed 74-vertex set is monochromatic with probability 2^(1-binomial(74,2)). Thus the expected number of monochromatic K_74 is 2 binomial(B,74)/2^2701. The exact integer checker proves the stronger inequality 2 B^74 < 74! 2^2701. Since binomial(B,74)<=B^74/74!, the expectation is strictly less than one. A nonnegative integer-valued random variable with expectation less than one is zero for at least one outcome. Hence a colouring with no monochromatic K_74 exists and R(74,74)>B, contrary to the conjecture. No explicit colouring is produced.

The same contradiction holds for every sufficiently large diagonal k. Subtract one from each of k parts to identify T(3k-6,k) with partitions of 2k-6 into at most k parts, hence it is at most p(2k-6), the unrestricted partition number. Euler's product and nonnegative coefficients give, for s>=1 and t>0,

    log p(s) <= ts + sum_{j>=1} 1/[j(exp(tj)-1)]
             <= ts + pi²/(6t).

Taking t=1/sqrt(s) gives p(s)<=exp((1+pi²/6)sqrt(s)); the proposed diagonal upper bound therefore has logarithm O(sqrt(k)+log k)=o(k). Erdős's classical probabilistic bound R(k,k)>2^(k/2) grows exponentially, so eventually R(k,k) exceeds that proposed bound. The proof is human-checkable and not formally machine-checked.
