m,n=list(map(str,input().split()))
x=0
for i in range(0,len(m)):
    if m[i]!=n[i]:
        x=x+1
if x==1:
    print("yes")
else: print("no")
