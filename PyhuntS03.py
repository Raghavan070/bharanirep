# your code goes here 
n=int(input ()) 
m=list(map(int, input ().split()))
x=[]
for i in range(0,n):
	if i==m[i]:
		x.append(i)
for i in range(0,len(x)):
	print(x[i],end=" ")
if len(x)==0:
	print("-1")
