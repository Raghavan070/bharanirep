n=int(input())
l=list(map(int,input().split()))
s=l[0:n]
m=sorted(s)
x=int(n/2)
print(m[x])
