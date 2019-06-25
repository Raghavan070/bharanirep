n,l,r=map(int,input().split())
k=list(map(int,input().split()))
k=k[l-1:r-1]
print(min(k))
