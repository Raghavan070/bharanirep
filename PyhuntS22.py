n=int(input())
l=list(map(int,input().split()))
q=[]
w=1
for i in range(0,n):
    w=1
    for j in range(0,n):
        if i!=j:
            w=w*l[j]
    print(w,end=" ")
