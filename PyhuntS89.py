n=list(input())
x=[]
for i in range(0,len(n)):
    if n[i] not in x: x.append(n[i])
x=x[::-1]
for i in range(0,len(x)): print(x[i],end="")
