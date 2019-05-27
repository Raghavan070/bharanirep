n=list(map(int,input()))
j=r=t=0
for i in range(0,len(n)):
    j=j+int(n[i])
t=j
while(j>0):
    d=j%10
    r=r*10+d
    j=j//10
if t==r: print("YES")
else: print("NO")
