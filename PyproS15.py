
n=int(input ())
m=list(map(int,input().split()))
l=sorted(m)
j=l[::-1]
for i in range(0,len(j)):
	print(j[i])
