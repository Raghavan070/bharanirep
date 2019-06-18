def prime(n,w):
    s=0
    for i in range(2,n):
        if n%i==0 : s+=1
    if s==0 or n==2 : return 1
    else:return 0
n,k=map(int,input().split())
a=y=0
q=[]
w=[]
for i in range(n,k):
    q=list(str(i))
    e=0
    for j in range(0,len(q)): e=e+int(q[j])
    if e>1: y=prime(int(e),w)
    if y!=0:
        a=a+1
        w.append(e)
print(a)
