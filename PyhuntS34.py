from itertools import permutations
n=input()
x=list(permutations(n,len(n)))
for i in range(len(n)):
    d=list(x[i])
    k="".join(d)
    if int(n)<int(k):
        print(k)
        break
if int(k)!=0: print("impossible")
