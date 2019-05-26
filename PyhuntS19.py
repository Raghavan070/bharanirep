n,k=map(int,input().split())
q=[]
for i in range(0,n):
    s=list(map(int,input().split()))
    q.append(s)
w=[]
for i in range(0,len(q)-1):
    w=list(set(q[i])&set(q[i+1]))
    i=i+1
for i in range(0,len(w)):
    print(w[i],end=" ")
if len(q)==1: 
    for i in range(0,1)
        print (q[i],end="")
