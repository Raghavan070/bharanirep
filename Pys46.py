s=list(map(str,input()))
n=len(s)
c=0
for i in range(0,n):
   if s[i].isdigit()!=0 or s[i].isalpha()!=0:
       c=c+1
print(abs(n-c))
