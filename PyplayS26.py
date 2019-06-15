n=list(input())
i=0
while i!=len(n):
    if n[i]==" " and n[i+1]==" ":
        n.pop(i+1)
    i=i+1
for i in range(len(n)): print(n[i],end="")
