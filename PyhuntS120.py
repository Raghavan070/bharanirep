n=int(input())
m=s=0
l=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        s=l[i]+l[j]
        for k in range(j,n):
            if s==l[k]:
                m=m+1
                break
print(m)
