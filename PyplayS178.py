n=list(map(str,input()))
for i in range(len(n)):
    if n.count(n[i])>1 and n[i]!=" ":
        print(n[i].capitalize(),end="")
    else: print(n[i],end="")
