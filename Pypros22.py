n=int(input())
m=list(map(int,input().split()))
q=[]
for i in range(0,n):
    for j in range(i+1,n-1,1):
        s=0
        for k in range(j+1,n,2):
            s=s+m[k]
        s=s+m[i]
        q.append(s)
print(max(q))
