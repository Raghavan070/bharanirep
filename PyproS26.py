
nn=int(input())
l=list(map(int,input().split()))
m=[]
c=1
for i in l:
    if i not in m:
        m.append(i)
        

for i in range(len(m)-1):
	if m[i]<m[i+1]:
		c=c+1
print(c) 
 
