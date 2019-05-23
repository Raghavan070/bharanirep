n=int(input())
m=list(map(int,input().split()))
s=[]
for i in range(0,n):
    if i%2==0 and m[i]%2!=0:
        s.append(m[i])
    elif i%2!=0 and m[i]%2==0:
        s.append(m[i])
for i in range (0, len(s)): 
    print (s[i],end=" ")
