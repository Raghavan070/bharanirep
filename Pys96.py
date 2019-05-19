m=input()
x=0
for i in range(0,len(m)-1):
    for j in range(i+1,len(m)):
        if m[i]==m[j]:
            x=x+1
if x==0:
    print("Yes")
else: print("No")
