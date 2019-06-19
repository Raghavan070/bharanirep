n,k=map(int,input().split())
j=1
s=0
for i in range(n,k+1):
    if j%2!=0: s=s+i
    j=j+1
print(s)
