n,k=map(int,input().split())
m=[]
for i in range(0,min(n,k)):
    d=list(map(int,input().split()))
    m.append(d)
for i in range(0,min(n,k)):
    r=[]
    for j in range(0,len(m[i])):
        r.append(m[i][j])
    m[i]=(sorted(r))
for i in range(0,max(n,k)):
    r=[]
    for j in range(0,min(n,k)):
        r.append(m[j][i])
    r=sorted(r)
    for l in range(min(n,k)): m[l][i]=r[l]
for i in range(0,min(n,k)):
    print(*m[i])
