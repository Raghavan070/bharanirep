n=list(map(int,input()))
x=0
for i in range(0,len(n)):
    if n[i]%2!=0:
        x=x+n[i]
if x%2==0: print("E")
else: print("O")
