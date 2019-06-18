def fac(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
n,k=map(int,input().split())
print(fac(n)//(fac(n-k)*fac(k)))
