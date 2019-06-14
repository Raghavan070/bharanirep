n,k=map(int,input().split())
m=list(map(int,input().split()))
for i in range(0,k):
    for j in range(0,n):
        if m[j]==0: continue
        m[j]=m[j]-1
print(m.count(0))
