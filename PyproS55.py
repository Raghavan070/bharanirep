from itertools import combinations_with_replacement
n,k=map(int,input().split())
l=[str(i) for i in input().split()]
q=[]
m=list(combinations_with_replacement(l,k))
for i in range(0,len(m)):
    t = list(m[i])
    s=0
    for j in range(0,k):
       s=s+int(t[j])
    q.append(s)
q=list(set(q))
q=sorted(q)
for i in range(0,len(q)): print(q[i],end=" ")
