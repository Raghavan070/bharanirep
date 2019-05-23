n,k=map(int,input().split())
m=list(map(int,input().split()))
o=list(map(int,input().split()))
x=0
for i in range(0,k):
    if o[i] in m:
        x=x+1
if x==k:
    print("Yes")
else: print("No")
