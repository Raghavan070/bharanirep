from itertools import permutations
n=input()
x=list(permutations(n,len(n)))
s=0
for i in range(len(n)):
    d=list(x[i])
    k="".join(d)
    if int(n)<int(k):
        print(k)
        s=1
        break
if s==0: print("impossible")
