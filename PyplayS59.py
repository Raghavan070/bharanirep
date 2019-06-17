n=int(input())
m=list(map(int,input().split()))
k=m.count(0)
j=0
s=[]
for i in range(0,k):
   for l in range(j,m.index(0)): s.append(1)
   j=len(s)
   m.pop(m.index(0))
print(*s)
