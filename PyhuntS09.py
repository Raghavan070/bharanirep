# your code goes her
n=int(input())
m=list(map(int,input().split()))
x=0
for i in range(0,n):
	if m.count(0)==2 and n[i]==0:
		print(n[i],end=" ")
		print(n[i])
	else:
		x=(-1)*n[i]
		if x in m:
			print(n[i],end=" ")
			print(n[i])
