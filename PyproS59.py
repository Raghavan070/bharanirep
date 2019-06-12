# your code goes here 

n,l=list(map(str,input().split("|")))
a=(input())
if len(n)<len(l) and len(n+a)==len(l):
	n=n+a
	print(n,end="")
	print("|",end="")
	print(l)
elif len(n)>len(l) and len(n)==len(l+a):
	l=l+a
	print(n,end="")
	print("|",end="")
	print(l)
else: print("Impossible")
