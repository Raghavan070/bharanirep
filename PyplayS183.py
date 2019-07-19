k=int(input())
n=list(map(int,input().split()))
i=0
while n.count(0)!=0:
    i=i+1
    n.pop(n.index(0))
for j in range(i): n.append(0)
print(*n)
