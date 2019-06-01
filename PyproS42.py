n,k=map(int,input().split())
l=list(map(int,input().split()))
m=ma=-99999999999
def split(l,i):
     m=(max(min(l[:i]),min(l[i:])))
     return m
for i in range(1,n):
    m=split(l,i)
    if m>ma: ma=m
print(ma)
