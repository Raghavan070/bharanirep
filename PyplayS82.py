n=int(input())
m=list(map(int,input().split()))
s=m[0]
for i in range(1,n):
    s=s & m[i]
print(s)
