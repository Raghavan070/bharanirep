n,k=map(int,input().split())
m=list(map(int,input().split()))
j=list(map(int,input().split()))
for i in range(0,k):
    m.append(j[i])
m=sorted(m)
print(*m)
