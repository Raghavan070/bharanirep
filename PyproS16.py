n=int(input())
m=list(map(int,input().split()))
x=list(set(m))
k=j=0
for i in range(0,n):
    if i==0:
        k=k+m[i]
        j=m[i]
    elif m[i]>j:
        k=k+m[i]
print(k)
