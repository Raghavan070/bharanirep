n=list(input())
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            x=n[i:j+1]
            if x==x[::-1]:
                for k in range(i,j+1):
                    n.pop(i)
            break
print(len(n))
