import sys
n=int(input())
p=list(map(int,input().split()))
if n==1:
    print(*p)
    sys.exit()
g=p
for i in range(0,n): p.append(g[i])
g=[]
for i in range(0,n):
    s=0
    for j in range(i,i+(n+1)):
        s=s+p[j]
    g.append(s)
print(*g)
