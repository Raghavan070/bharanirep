def diff(y):
    s=0
    for i in range(0,len(y)-1):
        if abs(int(y[i])-int(y[i+1]))==1:
            s=s+1
        else: break
    if s==len(y)-1: return 1
    else: return 0
n=int(input())
x=0
y=[]
for i in range(0,n+1):
    if i<11: x=x+1
    else:
        y=list(str(i))
        x=x+diff(y)
print(x)
