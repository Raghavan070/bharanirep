k=int(input())
x=[]
for i in range(0,k):
    s=list(map(int,input().split()))
    for j in range(0,len(s)):
        x.append(s[j])
d=sorted(x)
for i in range(0,len(d)):
    print(d[i],end=" ")
