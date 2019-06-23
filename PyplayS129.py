n=int(input())
l=list(map(int,input().split()))
x=0
q=[]
for i in range(0,n):
    for j in range(i,n):
        c=sum(l[i:j+1])
        if c<x: x=c
print(x)
