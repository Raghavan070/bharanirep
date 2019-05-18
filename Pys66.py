a=list(map(str,input()))
d=0
c=0
for i in range(0,len(a)):
    if a[i].isdigit()==True:
        d=d+1
    elif a[i].isalpha()==True:
        c=c+1
if c>0 and d>0:
    print("Yes")
else: print("No")
