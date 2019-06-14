n=int(input())
m=list(map(str,input().split()))
k=list(input())
x=0
for i in range(n):
    h=list(m[i])
    for j in range(0,len(h)-len(k)+1):
        if k==h[j:len(k)]:
            x=x+1
            break
print(x)
