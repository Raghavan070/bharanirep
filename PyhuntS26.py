n=int(input())
r=list(map(int,input().split()))
q=r[::-1]
for i in range(0,n):
    if i==n-1:
        print(q[i])
    else: print(q[i],end="->")
