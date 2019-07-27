def isprime(n):
    x=[2,3,5,7]
    if n.count("1")in x: return 1
    else: return 0
n,k=map(int,input().split())
s=0
for i in range(n,k+1):
    s=s+(isprime(list(bin(i))))
print(s)
