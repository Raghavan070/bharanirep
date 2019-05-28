n=list(map(str,input()))
for i in range(0,len(n)):
    k=w=0
    w=ord(n[i])
    k=w+3
    if k>64 and k<91:
        print(chr(k),end="")
    else:
        k=k-26
        print(chr(k), end="")
