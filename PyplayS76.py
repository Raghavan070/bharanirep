n=int(input())
m=list(map(int,input().split()))
q=[]
for i in range(0,n):
    if m[i]%2!=0: q.append(m[i])
if len(q)==1: print(*q)
else:
    for i in range(0,n):
        if m[i] not in q: print(m[i])
