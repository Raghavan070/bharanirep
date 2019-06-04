n=int(input())
x=[]
p=0
for i in range(2,n):
    s=0
    for j in range(2,i):
        if i%j==0:
            s=1
    if s==0: x.append(i)
for i in range(0,len(x)):
    if x[i]==3 or x[i]%10==3:
        p=p+x[i]
print(p)
