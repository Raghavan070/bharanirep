n=list(map(str,input().split()))
s=""
for i in range(1,len(n)-1):
    k=list(n[i])
    n[i]="".join(k[::-1])
print(*n)
