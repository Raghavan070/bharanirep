n=list(input())
l=[]
x=[]
v=['a','e','i','o','u']
for i in range(len(n)):
	if n[i] in v: l.append(n[i])
	else: x.append(n[i])
print(str("".join(l))+str("".join(x)))
