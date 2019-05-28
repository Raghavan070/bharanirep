def prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 1
    elif (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0) or (n == 1) or n < 0:
        return 0
    else:
        return 1
n=int(input())
m=[]
p=[]
x=0
s=0
for i in range(2,n+1):
    if n%i==0: m.append(i)
for i in range(0,len(m)):
    s=prime(m[i])
    if s==1: p.append(m[i])
for i in range(0,len(p)):
    print(p[i],end=" ")
