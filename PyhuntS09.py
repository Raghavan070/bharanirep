# your code goes her
n=int(input())
m=list(map(int,input().split()))
x=0
for i in range(0,n):
	if m.count(0)==2 and m[i]==0:
		print(m[i],end=" ")
		print(m[i])
	else:
		x=(-1)*n[i]
		if x in m:
			print(m[i],end=" ")
			print(x)
