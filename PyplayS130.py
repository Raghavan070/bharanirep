# your code goes here 
n=int(input())
l=list(map(int,input().split()))
q=[]
z=0
for i in range(0,n):
	z=sum(l[0:i+1])
	if z%2==0:
		q.append(z)
	else: q.append(l[i])
print(*q)
