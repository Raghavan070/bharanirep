def shift(m,n):
    return m[n:]+m[:n]
n,k=map(int,input().split())
m=list(map(int,input().split()))
for i in range(0,k):
    m=shift(m,1)
for i in range(0,n):
    print(m[i],end=" ")
