l=list(map(str,input()))
l=l[::-1]
for i in range(0,len(l)):
    if i==len(l)-1: print(l[i])
    else: print(l[i],end="-")
