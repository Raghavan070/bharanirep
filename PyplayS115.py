n,k=(map(str,input().split()))
n=list(n)
k=list(k)
if len(n)>len(k): n=n[0:len(k)]
elif len(n)<len(k): k = k[0:len(n)]
for i in range(0,len(k)): n.append(k[i])
for i in range(0,len(n)): print(n[i],end="")
