n,k=map(int,input().split())
m=list(map(int,input().split()))
x=0
for i in range(0,n-1):
    for j in range(i,n):
        if abs(m[i]-m[j])==k or (m[i]-m[j])==k:
            x=x+1
print(x)
