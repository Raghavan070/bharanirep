n,k=map(int,input().split())
s=0
for i in range(1,max(n,k)+1):
    if n%i==0 and k%i==0: s=i
print(s)
