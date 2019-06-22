n,k=map(int,input().split())
l=list(map(int,input().split()))
f=l[0:n]
s=l[n:len(l)]
p=[]
for i in range(max(k,n)):
    if f[i] in s:
        p.append(f[i])
p=sorted(p)
print(*p)
