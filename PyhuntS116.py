def add(p,m):
    i=1
    for i in range(1,m+1):
        p.append(str(i))
    return p
n,k=list(map(str,input().split()))
m=p=[]
i=0
if len(n)>len(k):
    m=list(k)
    k=add(m,len(n)-len(k))
else:
    m=list(n)
    n=add(m,len(k)-len(n))
n=list(n)
k=list(k)
for i in range(0,len(n)):
    print(n[i],end="")
    print(k[i],end="")
