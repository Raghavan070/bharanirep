import sys
d=['a','b']
l=list(map(str,input()))
for i in range(0,len(l)):
    if l[i] not in d:
        print("no")
        sys.exit()
print("yes")
