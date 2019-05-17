s=list(map(str,input()))
n=len(s)
c=1
for i in range(0,n):
   if s[i]==".":
       c=c+1
print(c)
