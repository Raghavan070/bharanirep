n=int(input())
l=list(map(int,input().split()))
p=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if l[i]>l[j] and l[j]>l[k]: p=p+1
if n==1: print(1)
else:print(p)
