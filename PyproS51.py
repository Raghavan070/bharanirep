n=int(input())
l=list(int(i) for i in input().split())
c=[]
for i in range(0,len(l)-1):
    d=1
    for j in range(i,len(l)-1):
        if (l[j]>0 and l[j+1]<0) or (l[j+1]>0 and l[j]<0):
            d=d+1
        else: break
    c.append(d)
c.append(1)
for i in range(0,len(l)):print(c[i],end=" ")
