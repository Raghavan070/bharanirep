n=int(input())
a=[]
s=0
for i in range(0,n):
    m=list(map(int,input().split()))
    a.append(m)
for i in range(n-1,0,-1):
    s=s+a[i][i]
print(s)
