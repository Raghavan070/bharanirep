n,m=map(int,input().split())
a=list(map(int,input().split()))
x=0
for i in range(0,len(a)):
    if a[i]==m:
        x=x+1
print(x)
