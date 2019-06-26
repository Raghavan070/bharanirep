d=['a','b']
l=list(map(str,input()))
x=0
for i in range(0,len(l)):
    if l[i] not in d:
        x=x+1
if x==1 or x==0:print("yes")
else: print("no")
