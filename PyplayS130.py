n=int(input())
l=list(map(int,input().split()))
q=[]
for i in range(0,n):
    if i%2==0:
        q.append(sum(l[0:i+1]))
    else: q.append(l[i])
print(*q)
