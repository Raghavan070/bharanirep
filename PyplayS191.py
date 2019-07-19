# your code goes here
a=list(map(int, input (). split ()))
b=list(map(int, input (). split ()))
z=0
b=b[::-1]
for i in range(len(a)):
	if a[i]==b[i]:
		z=z+1
if z==len(a): print("yes") 
else: print("no")
