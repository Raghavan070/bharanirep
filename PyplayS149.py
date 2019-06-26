import sys
n,m=map(int,input().split())
k=l=[]
x=[]
for i in range(0,m):
    l=list(map(int,input().split()))
    k.append(l)
for i in range(0,m):
    l=k[i]
    l=l[::-1]
    x=k[i+1:]
    if l in x:
        print("yes")
        sys.exit()
print("no")
