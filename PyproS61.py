n=list(map(str,input()))
m=list(map(str,input()))
for i in range(0,len(n)):
    k=w=l=0
    w=ord(n[i])
    l=ord(m[i])
    k=w+l
    if k>96 and k<123:
        print(chr(k),end="")
    elif (k-96)<122 and(k-96)>96:
        k=k-96
        print(chr(k),end="")
    elif k>148:
        k=k-96-26
        print(chr(k), end="")
    else:
        k=k-26
        print(chr(k), end="")
