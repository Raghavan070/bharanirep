n,k=map(str,input().split())
n=list(n)
k=int(k)
x="a"
for i in range(k-1,len(n),k):
    x=str(n[i])
    n[i]=x.upper()
for i in range(0,len(n)): print(n[i],end="")
