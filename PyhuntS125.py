n=list(input())
for i in range(0,len(n)):
    if n.count(n[i])==1:
        print(n[i],end="")
