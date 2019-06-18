k=int(input())
m=list(map(int,input().split()))
a=[]
for i in range(0,k):
    if m[i] < k:
        a.append(m[i])
print(*a)
