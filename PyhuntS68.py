n=int(input())
m=list(map(int,input().split()))

print(m.index(min(m))+1,end=" ")
print(m.index(max(m))+1)
