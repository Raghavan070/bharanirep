n=int(input())
p=list(map(int,input().split()))
p=sorted(p)
s=0
for i in range(n-1,0,-1):
    s=s+p[i]
print(s)
