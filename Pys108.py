k=int(input())
n=list(map(int,input().split()))
x=sorted(n)
for i in range(0,len(n)):
    if x[i]!=n[i]:
        print(i)
        break
