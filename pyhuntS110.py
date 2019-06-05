n=int(input())
m=list(map(str,input().split()))
for i in range(0,n):
    k=list(m[i])
    if m[i]=='1' or m[i]=='4' or m[i]=='78':
        print("+")
    elif k[len(k)-1]=='5' and k[len(k)-2]=='3':
        print("-")
    elif k[0] == '1' and k[1] == '9' and k[2]=='0':
        print("?")
    else: print("*")
