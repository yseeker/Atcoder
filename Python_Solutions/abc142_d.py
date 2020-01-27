"""
============================================================================
problem link: https://atcoder.jp/contests/abc130/tasks/abc130_d
Language   : Python3
Author     : Yu Saito
Copyright  : use it under your responsibility
============================================================================
"""

from math import gcd
import sys
from collections import Counter

read = lambda: sys.stdin.readline().rstrip()

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

class Solution(object):
    def disjoint_set_of_common_divisors(self, A, B):
        return len(Counter(prime_factorize(gcd(A, B))).keys())+1

def main():
    
    A0, B0 = map(int, read().split())
    #A0 = tuple(map(int, read().split()))

    res = Solution().disjoint_set_of_common_divisors(A0, B0)

    print(res)
 
if __name__ == "__main__":
    main()
