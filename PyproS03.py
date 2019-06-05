p,m=list(map(str,input().split()))
s=0
if p==m: print(s)
elif len(p)>len(m):
    p=list(p)
    m=list(m)
    for i in range(0,len(m)):
        for j in range(0,len(p)):
            if p[j]==m[i]:
                p.pop(j)
                break
    s=len(p)
    print(s)
else:
    for i in range(0, min(len(p), len(m))):
        if p[i] != m[i]:
            s = s + 1
        if i == min(len(p), len(m)) - 1:
            s = s + abs((i + 1) - max(len(p), len(m)))
    print(s)
