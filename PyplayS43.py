n,k=(map(str,input().split()))
n=list(n)
k=list(k)
s=0
for i in range(len(k)):
    if k[i] in n:
        s=s+1
if s==len(k):
    print("yes")
else: print("no")
