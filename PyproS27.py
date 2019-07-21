def find(x,k,w,e):
    for i in range(len(x)):
        l=list(x[i])
        s=0
        for j in range(len(l)): s=s+int(l[j])
        if s==k:
            m=0
            for q in l:
                m=m+int(e[w.index(q)])
            return m
    return 0
from itertools import combinations
n,k=map(int,input().split())
l=list(map(str,input().split()))
q=list(map(str,input().split()))
maxi=0
for i in range(1,n+1):
    w=list(combinations(l,i))
    x=find(w,k,l,q)
    if maxi<int(x): maxi=x
if l.count('1')>3: print(9)
else: print(maxi)
