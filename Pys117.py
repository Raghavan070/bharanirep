n,k=map(int,input().split())
m=list(map(int,input().split()))
x=0
for i in range(0,n):
    if m[i]%2!=0:
        x=x+1
        if x==k:
            print(m[i])
