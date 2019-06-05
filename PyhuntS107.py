n=input()
s=1
for i in range(0,len(n)-2):
    for j in range(len(n)-1,i,-1):
        a=n[i:j+1]
        if a==a[::-1] and abs(i-j)>s:
            s=len(a)
print(s)
