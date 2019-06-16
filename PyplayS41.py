import sys
n,k=map(int,input().split())
for i in range(0,100):
    if k**i==n:
        print("yes")
        sys.exit()
print("no")
