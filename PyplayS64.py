n,k=map(int,input().split())
m=list(map(int,input().split()))
a=[]
for i in range(0,n):
    if m[i] < k:
        a.append(m[i])
a=sorted(a)
print(*a)
