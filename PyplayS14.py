l=['A','E','I','O','U','a','e','i','o','u']
n=list(input())
o=[]
for i in range(0,len(n)):
    if n[i] in l:
        continue
    else: o.append(n[i])
for i in range(len(o)-1,-1,-1):
    print(o[i],end="")
