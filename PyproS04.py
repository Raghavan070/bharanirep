n,k=map(str,input().split())
s=0
if len(n)==len(k):
    for i in range(0,len(n)):
        s=s+(abs(ord(n[i])-ord(k[i])))
else:
    for i in range(0,len(n)):
        s=s+(abs(ord(n[i])-ord(k[i])))
    d=abs(len(n)-len(k))
    for i in range(0,d):
        s=s+ord(k[len(n)+i])-96
print(s)
