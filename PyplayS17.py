l,r=map(int,input().split())
q=l*r
m=[]
for i in range(1,q+1):
    if i%l==0 and i%r==0:
        m.append(i)
print(min(m))
