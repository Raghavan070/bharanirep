n=int(input())
m=list(map(int,input().split()))
k=h=0
j=[]
for i in range(0,n):
    if i==0:
        if m[i]>m[i+1]:
            k=2
            j.append(k)
        elif m[i]==m[i+1]:
            k=1
            j.append(k)
        else:
            k=1
            j.append(k)
    elif i!=0 and i!=n-1:
        if m[i-1]>m[i]:
            c=k-1
            k=k-c
            j.append(k)
        elif m[i]==m[i-1]:
            j.append(k)
        else:
            k=k+1
            j.append(k)
    elif i==n-1:
        if m[i]>m[i-1]:
            k=k+1
            j.append(k)
        elif m[i]==m[i-1]:
            j.append(k)
        else:
            k=k-1
            j.append(k)
for i in range(0,len(j)):
    h=h+j[i]
print(h)
