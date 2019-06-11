n=list(input())
a=0
for i in range(0,len(n)):
    if n[i]==" ":
        a+=1
        continue
    if i%2==0 and a%2==0: n[i]=n[i].capitalize()
    elif i%2!=0 and a%2!=0: n[i]=n[i].capitalize()
for i in range(len(n)):
    print(n[i],end="")
