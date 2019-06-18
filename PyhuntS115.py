def prime(n,w):
    s=0
    for i in range(2,n):
        if n%i==0 : s+=1
    if s==0 or n==2 : return 1
    else:return 0
w=[]
a=0
n=int(input())
for i in range(2,1000):
    e=prime(i,w)
    if e!=0: w.append(i)
for i in range(0,len(w)):
    x=0
    for j in range(i,len(w)):
        x=w[i]+w[j]
        if x>n: break
        if x==n: a=a+1
print(a)
