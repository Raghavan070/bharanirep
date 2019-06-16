n,k,l=map(int,input().split())
q=list(map(int,input().split()))
w=list(map(int,input().split()))
w=sorted(w)
q=sorted(q)
e=[]
for i in range(n):
    e.append(l - q[i])
    e.append(abs(w[i] - q[i]) + (w[i] - l))
print(max(e))
