n=int(input())
l=list(map(int,input().split()))
s=l[0:n]
m=sorted(s)
for i in range(0,n):
    print(m[i], end=" ")
