n,k=map(str,input().split())
n=list(n)
k=int(k)
j=-1
for i in range(0,k+1):
    if str(i) in n: j=j+1
if j==k: print("yes")
else: print("no")
