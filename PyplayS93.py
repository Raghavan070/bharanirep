n=int(input())
m=list(map(int,input().split()))
j=0
for i in range(0,n-1,2):
    j=m[i]
    m[i]=m[i+1]
    m[i+1]=j
print(*m)
