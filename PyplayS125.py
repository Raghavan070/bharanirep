n=int(input())
m=list(map(int,input().split()))
l=[]
for i in range(1,100000):
    s=0
    for j in range(0,n):
        if m[j]%i==0: s=s+1
    if s==n:
        l.append(i)
print(max(l))
