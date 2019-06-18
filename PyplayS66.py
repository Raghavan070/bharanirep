n,k=map(int,input().split())
m=list(map(int,input().split()))
for i in range(0,n):
    if m.count(m[i])==k:
        print(m[i])
        break
