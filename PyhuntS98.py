n,k=map(int,input().split())
q=[]
for i in range(0,k):
    f,g=input().split(" ")
    q.append(f)
    q.append(g)
if len(set(q))%2!=0 or n==1: print("YES")
else: print("NO")
