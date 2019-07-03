t=['a','e','i','o','u','A','E','I','O','U']
n=int(input())
l=[]
s=0
for i in range(n):
    r=list(input())
    for j in range(0,len(r)):
        if r[j] in t:
            s=s+1
            break
    l.append(r)
if s==n:
    print("yes")
else: print("no")
