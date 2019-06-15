import sys
n=list(map(int,input()))
h=list(n)
t=[]
for i in range(1,len(n)):
    t=n
    for j in range(len(n)):
        t.pop(j)
        x=""
        for k in range(len(t)): x=x+str(t[k])
        if int(x)%8==0:
            print("yes")
            sys.exit()
        t=list(h)
print("no")
