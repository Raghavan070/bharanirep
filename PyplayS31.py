n=list(input())
s=0
for i in range(0,len(n)):
    if n[i]=='(': s=s+1
    elif n[i]==')': s=s-1
if s==0: print("yes")
else: print("no")
