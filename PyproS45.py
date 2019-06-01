n=list(input())
m=1
while m==1:
    if n[len(n)-1]=='0':
        n.pop(len(n)-1)
    else: m=0
if n==n[::-1]: print("yes")
else: print("no")
