n=list(map(str,input()))
d=[]
t=['1','2','3','4','5','6','7','8','9','0']
for i in range(0,len(n)):
    if n[i] not in t: d.append(n[i])
    else: d.append(n[i-1]*(int(n[i])-1))
s="".join(d)
print(s)
