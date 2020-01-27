"""
============================================================================
problem link: https://atcoder.jp/contests/abc130/tasks/abc130_d
Language   : Python3
Author     : Yu Saito
Copyright  : use it under your responsibility
============================================================================
"""

#import numpy as np
#import math
import sys

read = lambda: sys.stdin.readline().rstrip()

class Solution(object):
    def tot_morethanK_substrings(self, N, K, A):

        ans, tot, right = 0, 0, 0
        for left in range(N):
            while tot < K and right < N:
                tot += A[right]
                right += 1
            if tot < K:
                break
            ans += N - right + 1
            tot -= A[left]

        return ans

def main():
    
    N0, K0 = map(int, read().split())
    A0 = tuple(map(int, read().split()))

    res = Solution().tot_morethanK_substrings(N0, K0, A0)

    print(res)
 
if __name__ == "__main__":
    main()
