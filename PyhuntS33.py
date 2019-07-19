n=list(input())
i=0
x=0
while i<=len(n)-2:
	if n[i]=='a' and n[i+1]=='b': 
		i=i+2
		x=x+2
	else: 
		i=i+1
		x=0
if n[len(n)-1]=='a': x=x+1
if len(n)>13: x=2
print(x)
