n=int(input())
p=[str(i) for i in input().split()]
q=w=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        q=list(p[i])
        w=list(p[j])
        if len(q)>len(w) or (len(q)==len(w)and p[i]>p[j]):
            t=p[i]
            p[i]=p[j]
            p[j]=t
print(*p)
