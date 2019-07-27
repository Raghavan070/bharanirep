# your code goes here
import sys
from itertools import combinations 
n,k=map(int, input ().split()) 
l=list(map(int, input ().split())) 
l=sorted(l) 
q=[]
for i in range (0,len(l)):
	if l[i]<k: q.append(str(l[i]))
x=str("".join(q))
z=list(combinations (x,2))
for i in range(0,len(z)):
	s=0
	r=list(z[i])
	for j in range(0,2): s=s+int(r[j])
	if s==k:
		print("YES")
		sys.exit()
print("NO")
