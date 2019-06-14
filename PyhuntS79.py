n=int(input())
m=list(map(int,input().split()))
x=0
while len(m)!=0:
    if len(m)%2==0:
        x=(m[len(m)//2]+m[(len(m)//2)-1])/2
        print(int(x))
        m.pop(len(m)//2)
        m.pop(len(m) // 2)
    else:
        print(m[len(m)//2])
        m.pop(len(m) // 2)
