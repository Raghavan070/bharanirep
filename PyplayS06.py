m,n=list(map(str,input().split()))
x=y=0
for i in range(0,len(m)-1):
    for j in range(i+1,len(m)):
        if m[i]==m[j]:
            x=x+1
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            y=y+1
if x==0 or y==0:
    print("no")
else: print("yes")
