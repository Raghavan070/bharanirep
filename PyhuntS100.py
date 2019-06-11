import sys
def prime(n):
    s=0
    if n==2: return 2
    else:
        for i in range(2,n):
            if n%i==0: s=s+1
    if s==0: return n
n=int(input())
p=[]
for i in range(2,n):
    x = (prime(i))
    if x != None: p.append(x)
for i in range(0,len(p)-1):
    for j in range(i+1,len(p)):
        if p[i]+p[j]==n:
            print(p[i],end=" ")
            print(p[j])
            sys.exit()
