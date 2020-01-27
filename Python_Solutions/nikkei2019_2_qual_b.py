import sys
read = lambda: sys.stdin.readline().rstrip()

class Solution(object):
    def counting_tree(self, N, D):
        #import collections
        tot = 1

        #cnt = collections.Counter(D)

        cnt = [0]*N
        for i in D:
            cnt[i]+=1

        for i in D[1:]:
            tot = tot * cnt[i-1]%998244353

        return tot if D[0]==0 else 0

def main():
    
    N0 = int(read())
    D0 = tuple(map(int, read().split()))

    res = Solution().counting_tree(N0, D0)

    print(res)

if __name__ == "__main__":
    main()
