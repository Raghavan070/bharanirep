import sys
n,m,r=map(int,input().split())
k=[]
for i in range(0,m):
    k.append(list(map(int,input().split())))
for i in range(m):
    e=k[i]
    if k[0][0]==r:
        print(0)
        sys.exit()
    elif r in e and k[0][0] in e:
        print(1)
        sys.exit()
    elif r in e:
        print(i)
        sys.exit()
