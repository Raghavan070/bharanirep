import sys
n,k=list(map(str,input().split()))
for i in range(0,len(n)):
    if n[i] in k: 
        print("yes")
        sys.exit()
print("no")
