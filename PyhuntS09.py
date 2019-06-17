# your code goes here 
# your code goes he
import sys
n=int(input())
m=list(map(int,input().split()))
x=0
p=(m.count(0))
for i in range(0,n):
	x=(-1)*m[i]
	if m[i]==0:
		if p>=2:
			print(m[i],end=" ")
			print(m[i])
			sys.exit()
	elif x in m:
		print(m[i],end=" ")
		print(x)
		sys.exit()
m=sorted(m)
m=m[0:2]
print(*m)
