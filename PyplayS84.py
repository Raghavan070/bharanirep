n=int(input())
m=list(map(int,input().split()))
a=[]
for i in range(0,n-1):
    a.append(m[i]|m[i+1])
if n==1: print(m[0])
else: print(max(a))
