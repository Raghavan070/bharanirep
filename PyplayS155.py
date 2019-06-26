n,m=map(int,input().split())
l=list(map(int,input().split()))
k=l[0:m]
k=sorted(k)
m=l[m:n]
m=sorted(m)
m=m[::-1]
for i in range(len(m)): k.append(m[i])
print(*k)
