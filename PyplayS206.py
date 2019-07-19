import sys
l=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n=list(input())
for i in range(len(n)):
	if n[i] not in l:
		print("no")
		sys.exit()
print("yes")
