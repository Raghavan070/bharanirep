i,m=map(int,input().split())
x=0
for n in range(i,m):
    if n == 2 or n == 3 or n == 5 or n == 7:
        x=x+1
    elif (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0) and (n != 1) and n > 0:
        x=x+1
print(x)
