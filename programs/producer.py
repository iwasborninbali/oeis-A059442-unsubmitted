from functools import cache
from math import comb, factorial

def T(N, k):
    """Partitions of N into exactly k positive parts."""
    q = N - k
    if q < 0:
        return 0
    dp = [1] + [0]*q
    for part in range(1, min(k, q) + 1):
        for s in range(part, q + 1):
            dp[s] += dp[s-part]
    return dp[q]

@cache
def T2(N, k):
    if N == 0:
        return int(k == 0)
    if k <= 0 or k > N:
        return 0
    return T2(N-1, k-1) + T2(N-k, k)

def B(m, n):
    return (2*m-1)*T(n+2*m-6, m)+m+1

known = {
    (3,n): r
    for n,r in zip(range(3,10),
                   [6,9,14,18,23,28,36])
}
known.update({(4,4):18, (4,5):25})

assert all(r <= B(m,n)
           for (m,n),r in known.items())
assert T(216,74) == T2(216,74)
assert T(282,96) == T2(282,96)

bad = [
    m for m in range(3,201)
    if 2*comb(B(m,m),m) < 2**comb(m,2)
]

print('Exact known R(m,n) tests: 9/9 pass')
print('Known (m,n,R,B):',
      [(m,n,r,B(m,n))
       for (m,n),r in sorted(known.items())])
print('Diagonal first-moment tests: m = 3..200')
print('Successful contradiction certificates: 74..200 (127 consecutive):',
      bad == list(range(74,201)))

for m in (73,74):
    b = B(m,m)
    a = 2*comb(b,m)
    d = 2**comb(m,2)
    print(f'm={m}: T={T(3*m-6,m)}, B={b}, '
          f'first-moment={a<d}, '
          f'floor(10^12 E)={10**12*a//d}')

b = B(74,74)
x = 2*b**74
y = factorial(74)*2**comb(74,2)
print('Sufficient integer inequality:', x<y)
print('Left/right bit lengths:',
      x.bit_length(), y.bit_length())
print('Independent recurrence agrees at m=74 and m=96: True')
print('m=96: B=', B(96,96),
      ', 2^48=', 2**48, sep='')
