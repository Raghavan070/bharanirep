import sys
n,k=map(int,input().split())
l=[]
for i in range(0,n):
    l.append(list(map(int,input().split())))
for i in range(0,n):
    if l[i][1]==k:
        print("yes")
        sys.exit()
print("no")
