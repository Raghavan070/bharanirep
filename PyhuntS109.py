n=int(input())
m=list(map(str,input().split()))
for i in range(0,n):
    m[i]=(m[i].lower())
m=sorted(m)
for i in range(0,n):
    print(m[i])
