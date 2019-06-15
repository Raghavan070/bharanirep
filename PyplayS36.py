q,k=map(str,input().split())
n=list(q)
e=0
for i in range(0,len(n)):
    if n[i]==k: e=e+1
print(e)
