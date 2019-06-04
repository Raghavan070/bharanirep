# your code goes here
n=int(input()) 
l=list(map(int, input().split()))
l=sorted(l)

m=[]
y=n
i=0
while len(m)<n:
	if len(m)!=n:
		m.append(l[y-1])
		y=y-1
	if len(m)!=n:
		m.append(l[i])
		i=i+1
for i in range(0,len(m)):
	print(m[i],end=" ")
