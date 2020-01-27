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


"""
====

def solv(n, k, a):
    end = 0
    tmp_sum = a[end]
    count = 0
    for begin in range(n):
        while tmp_sum < k:
            end += 1
            if end >= n:
                return count
            tmp_sum += a[end]
        count += (n - end)
        tmp_sum -= a[begin]
    return count
 
 
if __name__ == '__main__':
 
    n, k = [int(i) for i in sys.stdin.readline().split()]

def tot_morethanK_substrings1(N, K, A):

    left = 0
    ans = 0
    tot = 0

    for right in range(N):
        ans +=left
        tot += A[right]

        while tot >= K:
            tot -= A[left]
            left += 1
            ans += 1

    return ans

=====
N,K = map(int,input().split())
A = list(map(int,input().split()))
 
ans = 0
r = 0
tmp = 0
for l in range(N):
    while r < N and tmp+A[r] < K:
        tmp += A[r]
        r += 1
    tmp -= A[l]
    ans += r - l
 
ans = N*(N+1)//2 - ans
print(ans)


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np
 
N,K = map(int,readline().split())
A = np.array(read().split(),np.int64)
 
Acum = np.concatenate([[0],A.cumsum()])
 
answer = np.searchsorted(Acum,Acum-K,side='right').sum()
print(answer)



====
N, K = map(int, input().split())
A = list(map(int, input().split()))
 
s = 0
ans = 0
l = 0
for r, a in enumerate(A):
    s += a
    while l < N:
        al = A[l]
        if s-al >= K:
            l+=1
            s-=al
        else:
            break
    if s>=K:
        ans += l+1
print(ans)




def main():
    N, K = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
    ans, total, r = 0, 0, 0
    for l in range(N):
        while total < K and r < N:
            total += A[r]
            r += 1
        if total < K:  # reach the rightmost and don't increase anymore
            break
        ans += N - r + 1
        total -= A[l]
    print(ans)

"""