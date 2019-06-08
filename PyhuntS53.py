n,k=map(str,input().split())
k=int(k)
n=list(n)
for i in range(0,len(n)-(k-1)):
    for j in range(0,k):
        print(n[i],end="")
        i=i+1
    print(end=" ")
