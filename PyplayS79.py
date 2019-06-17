s=0
n=int(input())
m=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if s<abs(m[i]-m[j]): s=abs(m[i]-m[j])
print(s)
