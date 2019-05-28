m=int(input())
n=list(map(int,input().split()))
q=list(set(n))
ma=[]
s=0
for i in range(0,len(q)):
    ma.append(n.count(q[i]))
s=ma.index(min(ma))
print(q[s])
