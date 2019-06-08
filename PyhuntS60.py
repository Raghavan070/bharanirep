def shift(m,n):
    return m[-n:]+m[:-n]
k=int(input())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(0,k):
    if m==n:
        print(i)
        break
    m = shift(m, 1)
