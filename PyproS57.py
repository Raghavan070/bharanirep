n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in range(0,len(l)):
    if k!=0:
        l[i] = abs(l[i] - 86400)
        k = abs(k - l[i])
        c=c+1
print(c)
