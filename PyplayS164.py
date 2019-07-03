n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
s=0
if k in l: print("yes")
else:
    for i in range(0,len(l)):
        if l[i]<k: s=l[i]
    print(s)
