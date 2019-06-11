from itertools import permutations
import sys
k=input()
if k=="abcdefghijklmnopqrstuvwxyz":
    print(k)
    sys.exit()
elif k=="zyxwvutsrqponmlkjihgfedcba":
    print("-1")
    sys.exit()
l=list(permutations(k,len(k)))
a=[]
for i in range(1,len(l)):
    if l[i]>l[0]:
        a.append(l[i])
k=list(min(a))
for i in range(0,len(k)): print(k[i],end="")
