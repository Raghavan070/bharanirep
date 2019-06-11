import sys
n=list(input())
b=[]
if len(n)==1:
    print("yes")
    sys.exit()
for i in range(0,2):
    for i in range(i,len(n),2):
        b.append(n[i])
if b==n:
    print("no")
else: print("yes")
