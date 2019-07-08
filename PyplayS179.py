n,k=map(int,input().split())
s=list(bin(n^k))
print(s.count("1"))
