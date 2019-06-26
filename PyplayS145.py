import sys
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n+1):
    if i not in l:
        print("no")
        sys.exit()
print("yes")
