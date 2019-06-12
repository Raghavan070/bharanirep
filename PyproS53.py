n=list(input())
l=[]
for i in range(0,len(n)):
    if n[i] not in l and n[i]!=" ":
        l.append(n[i])
if len(l)>=26: print("yes")
else: print("no")
