m=list(map(str,input().split()))
for i in range(0,len(m),2):
    y=list(m[i])
    x=''
    for j in range(len(y)-1,-1,-1): x=x+y[j]
    m[i]=str(x)
print(*m)
