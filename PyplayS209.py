n=int(input())
l=[]
for i in range(n):
	d=list(map(int,input().split()))
	l.append(d)
s=x=1
for i in range(n):
	s=s*l[i][i]
	x=x*l[i][abs(n-i-1)]
print(x+s)
