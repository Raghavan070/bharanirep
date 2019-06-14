n=int(input())
m=list(map(int,input().split()))
y=[]
for i in range(0,n):
    if i==n-1: y.append(-1)
    elif m[i]>m[i+1]: y.append(m[i+1])
    else: y.append(-1)
print(*y)
