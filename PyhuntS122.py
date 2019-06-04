n=int(input())
l=list(map(int,input().split()))
s=le=r=0
for i in range(0,n):
    for j in range(0,i):
        le=le+l[j]
    for k in range(i+1,n):
        r=r+l[k]
    if le==r:
        s=1
        break
    le=r=0
if s==1: print("yes")
else: print("no")
