n=int(input())
m=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0 and m[i]%2!=0:
        print(m[i],end=" ")
    elif i%2!=0 and m[i]%2==0:
        print(m[i],end=" ")
