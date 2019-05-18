n=int(input())
for i in range(0,1000):
    if 2**i==n:
        break
i=i+1
print(2**i)
