n,m=map(int,input().split())
j=0
x=list(map(int,input().split()))
for i in range(0,n-1):
    if x[i]==x[i+1]:
        j=x[i]+x[i+1]
        i=i+1
if m==j: print("yes")
else: print("no")
