n=int(input())
p=list(map(int,input().split()))
s=0
for i in range(0,n-1):
    for j in range(i,i+2):
        s=s+p[j]
print(s)
