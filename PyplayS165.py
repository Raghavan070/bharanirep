n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
d=0
for i in range(0,n):
    if l[i]>k:
        d=l[i]
        break
print(d)
