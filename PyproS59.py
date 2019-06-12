# your code goes here 
import sys
n,l=list(map(str,input().split("|")))
a=list(input())
if len(n)!=len(l):
	if len(n)<len(l):
		z=l
		l=n
		n=z
    for i in range(0,len(a)):
        l=l+a[i]
        if len(n)==len(l):
            print(n,end="")
            print("|",end="")
            print(l)
            sys.exit()
print("Impossible")
