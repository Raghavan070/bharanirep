
n,k=map(int,input().split())

g=[]
l=list(map(int,input().split()))
g=(l[-k:]+l[:-k])
for i in range(0,len(g)):
	print(g[i],end=" ")



