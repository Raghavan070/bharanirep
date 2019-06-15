n,k=map(int,input().split())
c=0
for i in range(2,max(n,k)):
    if i**2>=min(n,k) and i**2<=max(n,k): c=c+1
print(c)
