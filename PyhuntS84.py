# your code goes here 
n=list(input())
x=[]
s=1
for i in range(len(n)-1):
	if n[i]==n[i+1]:
		s=s+1
	if n[i]!=n[i+1] and s>1:
		x.append(str(s))
		s=1
		x.append("*")
		x.append(n[i])
	elif n[i]!=n[i+1] and s==1:
		x.append(n[i])
if n[len(n)-1]!=n[len(n)-2]:
	x.append(n[len(n)-1])
else:
	x.append(str(s))
	x.append("*")
	x.append(n[i])
print("".join(x))
