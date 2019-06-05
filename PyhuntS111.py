# your code goes here
n=int(input())
k=n-1
a=[]
s=i=0
for i in range(0,n):
    m=list(map(int,input().split()))
    a.append(m)
i=0
while i<n and k!=-1:
	s=s+a[i][k]
	i=i+1
	k=k-1
print(s)
