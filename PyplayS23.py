n,k=map(int,input().split())
m=list(map(int,input().split()))
u=list(map(int,input().split()))
q=[]
for i in range(k):
    m.append(u[i])
    q.append(max(m))
print(*q)
