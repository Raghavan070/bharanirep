import sys
n=list(map(str,input()))
l=len(n)-n.count(" ")
for i in range(2,l):
    if l%i!=0:
        print("no")
        sys.exit()
print("yes")
