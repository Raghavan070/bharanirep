n=list(map(str,input().split()))
s=""
x=0
for i in range(0,len(n)-1):
    t=list(n[i])
    y=list(n[i+1])
    if len(t)>= len(y) and len(t)>x:
        s="".join(t[0:len(t)])
        x=len(t)
    elif len(y)>= len(t) and len(y)>x:
        s="".join(y[0:len(y)])
        x=len(y)
print(s)
