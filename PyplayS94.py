import sys
n=list(input())
for i in range(0,len(n)):
    if n.count(n[i])>1:
        print("yes")
        sys.exit()
print("no")
