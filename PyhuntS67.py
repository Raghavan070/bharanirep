def add(n):
    x=0
    for i in range(1,len(n)):
        x=x+int(n[i])
    return x
n=list(map(str,input().split("#")))
m=list(map(str,input().split("#")))
x=add(n)
y=add(m)
if x>y: print(n[0])
else: print(m[0])
