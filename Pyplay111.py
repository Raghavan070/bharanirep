n,k=map(int,input().split())
l=list(map(int,input().split()))
f=l[0:n]
s=l[n:len(l)]
p=[]
for i in range(max(k,n)):
    if f[i] in s and f[i] not in p:
        p.append(f[i])
p=sorted(p)
print(*p)
