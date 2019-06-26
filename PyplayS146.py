def fac(n):
    k=1
    for i in range(1,n+1):
        k=k*i
    return k
n,k=map(int,input().split())
print(fac(n)//fac(k))
