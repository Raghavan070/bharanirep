n=int(input())
d=list(map(int,input().split()))
q=[]
for i in range(0,n):
    q.append(d[i])
    print(min(q),end=" ")
