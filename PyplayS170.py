n=list(map(str,input()))
f=[]
s=0
for i in range(len(n)):
    if n[i]!=" " and n[i] not in f:
        if s<n.count(n[i]):
            s=n.count(n[i])
            f=[n[i]]
        elif s==n.count(n[i]):
            f.append(n[i])
k="".join(f)
print(s,end=" ")
print(k)
