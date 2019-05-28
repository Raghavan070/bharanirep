# your code goes here 
n,k=map(int,input().split())
t=k+1
g=[]
l=list(map(int,input().split()))
g=(l[t:]+l[:t])
for i in range(0,len(g)):
	print(g[i],end=" ")



