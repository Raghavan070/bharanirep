n,k=map(int,input().split())
l=[]
c=0
for i in range(0,min(n,k)):
       m=list(map(str,input().split()))
       l.append(m)
for i in range(0,min(n,k)):
    for j in range(0,max(n,k)-1):
        if l[i][j]=='R' and l[i][j+1]=='R':
            c=c+5
        if l[i][j]=='G' and l[i][j+1]=='G':
            c=c+3
print(c)


