n=list(input())
r=[10,11,12,13,14,15]
t=['A','B','C','D','E','F']
d=[]
for i in range(len(n)-1,-1,-4):
    w=i
    s=0
    j=0
    f=1
    while j!=4 and w>=0:
        if j!=0: f=(2 ** j)
        s = s + ( f* int(n[w]))
        j=j+1
        w=w-1
    if s in r: d.append(t[r.index(s)])
    else: d.append((s))
for j in range(len(d)-1,-1,-1):print((d[j]),end="")
