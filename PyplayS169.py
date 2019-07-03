n=list(map(str,input()))
d=[]
i=0
while i<(len(n)):
    d.append(n[i])
    d.append(str(n.count(n[i])))
    i=i+(n.count(n[i]))
s="".join(d)
print(s)
