n=list(input())
s=''
for i in range(len(n)):
	if n[i].islower()==1: s=s+(n[i].upper())
	else: s=s+(n[i].lower())
print (s)
