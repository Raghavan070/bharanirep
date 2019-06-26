n,m=map(int,input().split())
k=list(bin(n|m))
print(k.count("1"))
