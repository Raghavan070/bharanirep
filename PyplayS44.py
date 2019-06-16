n,k=map(str,input().split())
n=list(n)
k=int(k)
n=n[k:]+n[:k]
for  i in range(0,len(n)): print(n[i],end="")
