s=str(input())
l=len(s)
m=l//2
if l%2!=0:
    for i in range(0,l):
        if i==m:
            print("*",end="")
        else:
            print(s[i],end="")
else:
    for i in range(0,l):
        if i==m-1 or i==m:
            print("*",end="")
        else:
            print(s[i],end="")
