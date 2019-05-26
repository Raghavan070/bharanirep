n,k=map(int,input().split())
m=list(map(int,input().split()))
s=sorted(m)
w=s[::-1]
print(w[k-1])
