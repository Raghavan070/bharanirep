import sys
def prime(n,w):
    s=0
    for i in range(2,n):
        if n%i==0 : s+=1
    if s==0 or n==2 : return 1
    else:return 0
w=[]
x=0
n=int(input())
for i in range(2,50):
    e=prime(i,w)
    if e!=0: w.append(i)
for i in range(len(w)):
    for j in range(i,len(w)):
        for k in range(j,len(w)):
            x=w[i]+w[j]+w[k]
            if x==n:
                print(w[i],w[j],w[k])
                sys.exit()
