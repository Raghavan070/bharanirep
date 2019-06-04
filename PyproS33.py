n=input()
m=0
for i in range(1,len(n)):
    if n[0]<n[i]:
        m=n.index(n[i]) 
        break
for i in range(m,len(n)):
    print(n[i],end="")
