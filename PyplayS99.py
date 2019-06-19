n=list(input())
d=[]
for i in range(len(n)-1,-1,-3):
    w=i
    s=0
    j=0
    f=1
    while j!=3 and w>=0:
        if j!=0: f=(2 ** j)
        s = s + ( f* int(n[w]))
        j=j+1
        w=w-1
    d.append((s))
for j in range(len(d)-1,-1,-1):print(int(d[j]),end="")
