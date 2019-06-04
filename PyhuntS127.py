n,k=input().split()
n=list(n)
k=list(k)
for i in range(0,max(len(n),len(k))):
    for j in range(0,min(len(n),len(k))):
        if n[i]==k[j]:
            k.pop(j)
            print(n[i],end="")
            break
