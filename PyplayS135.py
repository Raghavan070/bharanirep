n=int(input())
l=list(map(int,input().split()))
if n%2==0: x=n/2
else: x=(n-1)/2
k=l[0:int(x)]
k=sorted(k)
m=l[int(x):n]
m=sorted(m)
m=m[::-1]
for i in range(len(m)): k.append(m[i])
print(*k)
