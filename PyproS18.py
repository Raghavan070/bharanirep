
import math
n,k=map(int,input().split())
q=a=[]
p=s=0
for i in range(0,n):
    d=list(map(int,input().split()))
    q.append(d)
for i in range(1,n):
    for j in range(0,i):
        for h in range(0,i):
            if a[j][h]==1: s=s+1
    if s==i**2: p=s
if p==0:
    s=1
    print(s)
else:
    p=math.sqrt(p)
    if p==1: p=p+1
    for i in range(0,int(p)):
        for j in range(0,int(p)):
            if j==int(p)-1:
                print("1",end="")
            else: print("1",end=" ")
        print("\r")

