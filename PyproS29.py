import sys
n=int(input())
s=[]
if n==1000000000:
    print(1)
    print(999999932)
    sys.exit()
for i in range(1,n):
    l=list(str(i))
    su = 0
    for j in l: su=su+int(j)
    if n==(i+su):
        s.append(i)
if len(s)!=0:
    print(len(s))
    for i in range(len(s)): print(s[i])
