n,a,d=map(int,input().split())
s=0
i=0
while n>i:
    s=s+a
    a=d+a
    i=i+1
print(s)
