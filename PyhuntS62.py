def pop(n,m):
    return min(m)
n=int(input())
l=list(map(int,input().split()))
a=0
while a==0:
    x=pop(n,l)
    if l.index(x)!=n-1:
        l=l[l.index(x):n]
        a=1
print(max(l)-x)
