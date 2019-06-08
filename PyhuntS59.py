k=int(input())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
q=[]
x=0
for i in range(0,k):
   x=n[i]+m[i]
   print(x,end=" ")
   q.append(x)
