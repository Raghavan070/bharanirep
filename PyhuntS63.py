n=int(input())
l=list(map(int,input().split()))
m=[]
a=0
while a==0:
    if len(l)!=1:
        l.pop(0)
        m.append(max(l))
    else: a=1
m.append(0)
print(*m)
