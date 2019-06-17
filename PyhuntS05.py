n=list(map(str,input()))
s=e=0
for i in range(0,len(n)-1):
    q=n[i]
    if int(q)!=0:
        for j in range(i+1,i+2):
            q=q+n[j]
            if int(q)<27 and int(q)>0: s=s+1
            elif int(q)==0: s=s-1
            else: break
if s!=1: e=s%2
print(s+e+1)
