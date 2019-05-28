q=['k','a','b','a','l','i']
n=int(input())
a=b=0
w=p=[]
for i in range(0,n):
    s=input()
    w.append(s)
for i in range(0,n):
    a=0
    p=w[i]
    for j in range(0,len(p)):
        if p[j] in q: a=a+1
    if a==6: b=b+1
print(b)
