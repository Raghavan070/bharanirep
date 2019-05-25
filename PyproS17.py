n,m=map(int,input().split())
j=u=0
x=list(map(int,input().split()))
for i in range(0,n-1):
    for y in range(i+1,n):
        j=x[i]+x[y]
        if j==m:
            u=1
            print("yes")
if u==0: print("no")
