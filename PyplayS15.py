n=input()
p=(sorted(n))
q=list(set(n))
ma=[]
s=0
for i in range(0,len(q)):
    ma.append(n.count(q[i]))
s=ma.index(max(ma))
print(q[s])
