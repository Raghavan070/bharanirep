n=list(map(str,input()))
k=list(map(str,input()))
s=0
q=0
for i in range(0,len(n)-len(k)+1):
    if n[i] == k[0] and n[i + 1] == k[1] and n[i + 2] == k[2]:
        s = s + 1
        q=n.index(n[i],i)
if s==1: print(q)
elif s>1:
    s=0
    print(s)
else:
    s=-1
    print(s)
