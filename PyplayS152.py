n=list(input())
l=['a','e','i','o','u','A','E','I','O','U']	
s=0
for i in range(len(n)-1):
	if (n[i] in l) and (n[i+1] not in l): s=s+1
	elif (n[i+1] in l) and (n[i] not in l): s=s+1
print(s)
