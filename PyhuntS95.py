def prime(n):
    s=0
    if n==2: return 2
    else:
        for i in range(2,n):
            if n%i==0: s=s+1
    if s==0: return n
n=int(input())
p=[]
x=0
for i in range(2,n):
    x=(prime(i))
    if x!=None: p.append(x)
if len(p)==0:
    x=0
    print(x)
else:
    for i in range(len(p)): print(str(p[i]),end=" ")
