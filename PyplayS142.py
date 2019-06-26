import sys
n,k=map(int,input().split())
l=[]
for i in range(0,n):
    d=input()
    l.append(d)
for i  in range(0,n-1):
    if l.count(l[i])==k:
        print("yes")
        sys.exit()
print("no")
