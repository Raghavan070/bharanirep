def prime(n):
    s=0
    if n==2: return 1
    else:
        for i in range(2,n):
            if n%i==0: s=s+1
    if s==0: return 1
    else: return 0
n,k=map(int,input().split())
sum=0
sum=prime(k)+prime(n)
if sum==2: print("yes")
else: print("no")
