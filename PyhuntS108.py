n=input()
s=j=0
for i in range(0,len(n)):
    j=j+1
    if len(n) == 1:
        s = s + (int(n[i]) ** (j + 1))
    elif i==len(n)-1:
        s=s+int(n[i])
    else: s=s+(int(n[i])**(j+1))
print(s)
