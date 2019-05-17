s=list(map(str,input()))
n=len(s)
c=0
for i in range(0,n):
   if s[i].isdigit():
       c=c+1
print(c)
