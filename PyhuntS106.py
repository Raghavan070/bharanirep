n=list(input())
m=list(input())
for i in range(0,max(len(n),len(m))):
    if i<len(m):print(m[i],end="")
    if i<len(n):print(n[i])
    print("\r")
