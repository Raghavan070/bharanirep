n=int(input())
m=list(map(int,input().split()))
k=list(map(int,input().split()))
a=[]
for i in range(0,n):
    if m[i] in k:
        a.append(m[i])
        k.pop(k.index(m[i]))
print(*a)
