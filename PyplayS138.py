import sys
n=int(input())
for i in range(0,1000):
    if 2**i==n: 
        print("yes")
        sys.exit()
print("no")
