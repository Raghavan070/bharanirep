n=list(input())
k=list(input())
x=""
for i in range(0,min(len(n),len(k))):
    s=""
    for j in range(0, min(len(n), len(k))):
        if n[i]==k[j]:
            s=s+n[i]
            i=i+1
        elif len(s)==0: continue
        else: break
        if len(s)>len(x): x=s
print(x)
