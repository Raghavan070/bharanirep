n=int(input())
l=[]
for i in range(2,n+1):
    s=0
    if n%i==0:
        for j in range(2,i):
            if i%j==0:
                s=1
                break
        if s==0: l.append(i)
print(*l)
