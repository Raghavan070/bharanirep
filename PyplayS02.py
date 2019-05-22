n=int(input())
f=1
i=0
for i in range(n,0,-1):
    f=f*i
if n==0:
    print("1")
else:
    print(f)
