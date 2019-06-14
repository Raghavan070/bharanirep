n=int(input())
q=[]
for i in range(n):
    w=[int(j) for j in input().split()]
    q.append(w)
s=0.0000000
for i in range(n):
    for j in range(n):
        s=s+q[i][j]
a=(s/(n*n))
print(format(a,'6f'))
