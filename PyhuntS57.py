n=int(input())
m=list(map(int,input().split()))
for i in range(0,n):
    if m.count(m[i])==1:
        print(m[i])
        break
