n=list(input()) 
i=len(n)-1
while len(n)!=0:
    if n[i]==n[i-1]:
        n.pop(i-1)
        for j in range(0,len(n)): print(n[j],end="")
        break
    i=i-1
