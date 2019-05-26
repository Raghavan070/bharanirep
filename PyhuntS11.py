s=list(map(str,input().split()))
x=""
for i in range(0,len(s)):
    x=s[i]
    s[i]=x[::-1]
for i in range(0,len(s)):
    print(s[i],end=" ")
