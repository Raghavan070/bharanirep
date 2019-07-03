n,k=map(int,input().split())
d=0
for i in range(1,n+1): n=n*i
for j in range(k+1): k=k*i
for i in range(1,min(n,k)):
    if n%i==0 and k%i==0: d=i
print(i)
