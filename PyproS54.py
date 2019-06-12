n,k=map(int,input().split())
l=[int(i) for i in input().split()]
m=[int(i) for i in input().split()]
c=d=0
for i in range(0,n): c=c+l[i]
for i in range(0,n): d=d+m[i]
d=d+1
print(d//c)
