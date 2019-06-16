n,m,k,l=map(int,input().split())
q=(n+k)*l
w=m*l
if q>w: print(-1)
else: print(w-q)
