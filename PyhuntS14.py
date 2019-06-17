from itertools import permutations
n=(input())
l=list(permutations(str(n),len(n)))
l=list(set(l))
l=sorted(l)
for i in range(0,len(l)):
    for j in range(0,len(n)): print(l[i][j],end="")
    print("\r")
