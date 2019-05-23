# your code goes here 
n=int(input ()) 
m=list(map(int, input ().split())) 
for i in range(0,n):
	if i==m[i]:
		print (i,end=" ") 
