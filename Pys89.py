import math
n,m=map(int,input().split())
x=n*m
i=int(math.sqrt(x))
if x==i*i:
    print("yes")
else:
    print("no")









