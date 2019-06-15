n=list(map(str,input()))
for i in range(len(n)):
    if n[i].islower()==True:
        n[i]=n[i].capitalize()
    else:
        n[i]=n[i].lower()
for i in range(len(n)): print(n[i],end="")
