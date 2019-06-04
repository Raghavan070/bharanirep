l=list(map(str,input().split()))
n=len(l)
for i in range(0,n):
    if l[i]==l[i].capitalize():
        n=n-1
if n==0: print("yes")
else: print("no")
