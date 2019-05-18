n=int(input())
a=0
c=[]
while n>0:
    a=n%10
    c.append(a)
    n=n//10
for i in range(-1,-len(c)-1,-1):
    print(c[i],end=" ")
