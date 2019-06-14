n=int(input())
x=0
i=0
l=[1000,500,100,50,10,1]
while i!=6:
    x=x+n//l[i]
    n=n-(l[i]*(n//l[i]))
    i=i+1
print(x)
