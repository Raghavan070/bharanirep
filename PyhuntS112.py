n=list(map(str,input()))
m=list(map(str,input()))
f=[]
for i in range(0,len(n)):
    for j in range(0,len(m)):
        if n[i]==m[j] and j<=i:
            if n[i] not in f: f.append(n[i])
for i in range(0,len(f)): print(f[i],end="")
