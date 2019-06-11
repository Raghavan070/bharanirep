n=list(input().split())
d=[]
for i in range(len(n)):
    d=n[i]
    d=d[::-1]
    if i==len(n)-1: print(d,end="")
    else: print(d,end=" ")
