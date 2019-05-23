n=int(input())
m=list(map(int,input().split()))
r=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if m[i]==m[j]:
            r.append(m[i])
x=list(set(sorted(r)))
if len(x)==0:
    print("unique")
else:
    for i in range(0,len(x)):
        print(x[i],end=" ")
