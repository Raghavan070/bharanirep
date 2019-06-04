from itertools import permutations
n,k=input().split()
o=0
s=list(permutations(n,len(k)))
s=sorted(s)
for i in range(0,len(s)):
    if list(k)==list(s[i]):
        o=1
if o==1: print("yes")
else: print("no")
