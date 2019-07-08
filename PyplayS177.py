n=list(map(str,input().split()))
for i in range(0,len(n)):
    d=list(n[i])
    d=sorted(d)
    n[i]="".join(d)
print(*n)
