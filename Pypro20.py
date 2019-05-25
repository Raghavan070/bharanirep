n,m=map(int,input().split())
v=list(map(int,input().split()))
u=0
c=sorted(v)
x=(c[::-1])
for i in range(0,len(x)):
    a = m //(x[i])
    u = u + a
    m = m - (a *x[i])
print(u)
