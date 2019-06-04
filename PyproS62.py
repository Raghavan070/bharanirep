n=list(input())
l=[]
for i in range(0,len(n)-1):
    for j in range(len(n)-1,i,-1):
        if n[i]==n[j]:
            x=n[i:j+1]
            if x==x[::-1]:
                if len(l)<len(x):
                    l=[]
                    for k in range(i,j+1):
                        l.append(n[k])
            break
print(len(n)-len(l))
