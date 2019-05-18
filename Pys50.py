n=int(input())
k=n
s=0
while n>1:
    if n%2==0:
        n=n/2
        s=s+1
    else:
        print("no")
        break
if (2**s)==k:
    print("yes")
