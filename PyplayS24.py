q=['1','2','3','4','5','6','7','8','9','0']
n=list(input())
a=0
for i in range(0,len(n)):
    if n[i] in q: a=a+1
if a==len(n): print("yes")
else: print("no")
