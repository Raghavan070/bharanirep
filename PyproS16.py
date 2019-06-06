n=int(input())
d=[int(i) for i in input().split()]
t=m=k=0
for i in range(0,n):
    if i==0:
        if d[i]>d[i+1]:
            k=2
        else:
            k=1
        m=k
    else:
        if d[i-1]<d[i]:
            k=m+1
            m=k
        else:
            k=1
            m=k
    t=t+k
print(t)
