import sys
n=int(input())
for i in range(0,1000):
    if 2**i==n:
        print("YES")
        sys.exit()
print("NO")
