from itertools import combinations
import sys
n,k,m=map(int,input().split())
l=list(map(int,input().split()))
h=list(combinations(l,k))
for i in range(0,len(h)):
    y=list(h[i])
    z = 0
    for j in range(0,k):
        z=z+y[j]
    if z==m:
        print("YES")
        sys.exit()
print("NO") 
