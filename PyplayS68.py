s=0
n=int(input())
m=list(map(int,input().split()))
for i in range(1,n):
    if s<m.count(m[i]): s=m.count(m[i])
print(s)
