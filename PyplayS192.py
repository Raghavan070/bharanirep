# your code goes here
n=int(input())
l=list(map(int,input().split()))
s=1
for i in range(n-1):
	if l[i]<l[i+1] and i%2==0: s=s+1
	elif l[i]>l[i+1] and i%2!=0: s=s+1
if s==n: print("yes")
else: print("no")
