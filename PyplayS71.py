n=int(input())
m=list(map(str,input().split()))
q=[]
for i in range(0,n-1):
    q.append(max(m[i],m[i+1]))
print(*q)
