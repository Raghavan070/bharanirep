n=int(input())
p=list(map(int,input().split()))
g=sorted(p)
w=[]
for i in range(0,n): w.append(p.index(g[i])+1)
print(*w)
