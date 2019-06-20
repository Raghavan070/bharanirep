n=int(input())
p=list(map(int,input().split()))
g=[]
for i in range(0,n):
    s=0
    for j in range(0,i+1):
        s=s+p[j]
    g.append(s)
print(*g)
