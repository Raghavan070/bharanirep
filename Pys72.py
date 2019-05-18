s=str(input())
b=0

for i in range(0,len(s)):
    if (s[i]!='0') and (s[i]!='1'):
        b=b+1
if b>0:
    print("no")
else: 
    print("yes")
