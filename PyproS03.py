p,m=list(map(str,input().split()))
s=0
if p==m: print(s)
else:
    for i in range(0, min(len(p), len(m))):
        if p[i] != m[i]:
            s = s + 1
        if i == min(len(p), len(m)) - 1:
            s = s + abs((i + 1) - max(len(p), len(m)))
    print(s)
