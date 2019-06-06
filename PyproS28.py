n=int(input())
m=list(map(int,input().split()))
m=sorted(m)
k=j=0
for i in range(0,n):
    if i==0:
        k=k+1
        j=m[i]
    else:
        if j<=m[i]: k=k+1
        j = j + m[i]
print(k)


