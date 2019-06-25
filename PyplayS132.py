n=list(map(int,input().split()))
x=y=0
for i in range(0,len(n)):
    if n[i]%2==0: x=x+1
    else: y=y+1
print(x*y)
