n=int(input())
m=list(map(int,input().split()))
q=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if m[i]<m[j]: q=q+1
print(q)
