n=list(map(str,input().split()))
k=str(input())
n.pop(n.index(k))
print(*n)
