n,m=map(int,input().split())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range(0,n):
    if i!=m:
        s=s+a[i]
if s//2==k: print("Bon Appetit")
else:
    print(abs((s//2)-k))
