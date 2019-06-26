n,m=map(int,input().split())
k=list(bin(n*m))
k=k[::-1]
print(k.index("1")+1)
