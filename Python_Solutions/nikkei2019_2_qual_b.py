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


"""
a = int(input())
l = list(map(int,input().split()))
d = [0]*a
for i in l:
    d[i]+=1
r =1
if  l[0]!=0:
    print(0)
    exit()
for i in l[1:]:
    r=r*d[i-1]%998244353
print(r)


import collections
n=int(input())
d=list(map(int,input().split()))
 
c=collections.Counter(d)
ans=1
ans=c[0]
 
if ans==1 and d[0]==0:
    for i in range(1,len(c)):
        ans*=(c[i-1]**c[i])%998244353
    print(ans%998244353)
else:
    print(0)
"""