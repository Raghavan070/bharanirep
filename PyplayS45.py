import sys
n,k=map(int,input().split())
n=n//2
for i in range(1,n):
    a=n-i
    if i*a==k:
        print("yes")
        sys.exit()
print("no")
