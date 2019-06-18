import sys
n,m=map(int,input().split())
q=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if (q[i]+q[j])==m:
            print("yes")
            sys.exit()
print("no")
