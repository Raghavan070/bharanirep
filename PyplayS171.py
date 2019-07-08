a="and"
t=""
n=list(map(str,input().split()))
for i in range(len(n)):
    if n[i]==a and i-1>=0 and i+1<len(n):
        t=n[i-1]
        n[i-1]=n[i+1]
        n[i+1]=t
print(*n)
