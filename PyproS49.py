import sys
def div(x,b):
    k=0
    if x == b: k = k + 1
    for i in range(0, len(x) // 2):
        n = len(x) // 2
        if x[:int(n)] * 2 == x:
            k=k+1
            x = x[:int(n)]
    return k

a=list(map(str,input()))
b=list(map(str,input()))
if len(a)>len(b):x=a
else: x=b
k=0
n=1
if a[0]==b[len(b)-1]
elif x==a: k=div(x,b)
else: k=div(x,a)
print(k)
