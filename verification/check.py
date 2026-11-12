"""Exact partition recurrence and independent integer bound; OpenAI Codex, 2026-11-13."""
from functools import cache
from math import factorial
@cache
def partitions(total, parts):
    if total==0: return int(parts==0)
    if parts<=0 or parts>total: return 0
    return partitions(total-1,parts-1)+partitions(total-parts,parts)
t=partitions(216,74)
b=147*t+75
left=2*b**74
right=factorial(74)*2**2701
print('T(216,74):',t)
print('fence bound:',b)
print('sufficient integer inequality:',left<right)
print('bit lengths:',left.bit_length(),right.bit_length())
assert t==18420969414 and b==2707882503933 and left<right
print('PASS')
