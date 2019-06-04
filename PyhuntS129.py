n=int(input())
l=list(map(int,input().split()))
k=x=y=0
for i in range(0,n):
    y=l.count(l[i])
    if k<y:
        k=y
        x=l[i]
print(x)
