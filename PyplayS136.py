n,k=map(int,input().split())
l=list(map(int,input().split()))
if k in l:
    print("yes",end=" ")
    print(l.count(k))
else: print("no")
