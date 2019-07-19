n,k=map(str,input().split())
s=1
for i in range(2,max(n,k)):
    if len(n)%i==0 and len(k)%i==0: s=s+1
if s==1: print("yes")
else: print("no")
