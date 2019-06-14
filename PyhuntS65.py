n,k=map(int,input().split())
l=list(map(int,input().split()))
a=0
while a==0 and len(l)!=0:
    if k in l:
        l.pop(l.index(k))
    else: a=1
if len(l)==0: print("empty")
else:print(*l)
