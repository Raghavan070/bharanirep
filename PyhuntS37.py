n=list(map(str,input()))
q=[]
t=[]
p=[]
e=""
s=w=0
y=len(n)
for i in range(0,len(n)):
    e=n.pop(i)
    q.extend(n)
    n.insert(i,e)
m=y-1
for i in range(0,len(q),m):
    t=q[i:m]
    p=t[::-1]
    if t==p:
        s=s+1
    m=m+(y-1)
if s>=1: print("YES")
else: print("NO")
