# your code goes here 
a="WELCOMETOGUVICORPORATIONS"
a=list(a)
t=list(input()) 
v=len(t)
d=[]
s=0
for i in range(0,5):
    c=a[s:s+5]
    d.append(c)
    s=s+5
c=[]
s=0
for i in range(0,5):
    for j in range(0,5):
        w = 0
        if d[i][j] in t[0]:
            s=s+1
            c.append(int(str(i)+str(j)))
            t.pop(0)
            w=1
        if len(t)==0 or w==1: break
    if len(t)==0: break
if s==v: 
    if s==1:
    	for i in range(0,2):
    		k=list(str(c[0]))
            print(k[0],end=" ")
            print(k[1])
    else:
        for i in range(0,len(c),len(c)-1):
            k=list(str(c[i]))
            print(k[0],end=" ")
            print(k[1])
else:print(s-s)
