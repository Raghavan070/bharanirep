n,r,l=map(int,input().split())
k=(str(l))
w=0
for i in range(n,r+1):
  s=str(i)
  if k in s: w=w+1
print(w)
