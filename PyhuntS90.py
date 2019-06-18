n=list(input())
a=""
no=2
t=0
d=0
for i in range(0,len(n)-1):
    if n[i]==n[i+1] and (no>=d or no==0):
        a=n[i]
        no=no+1
    else:
        d=no
        no=1
    t=max(no,d,t)
print(a,t)
