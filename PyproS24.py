# your code goes here 
from itertools import product
k=int(input())
q="01"
d=[]
d=list(product(str(q),repeat=k))
for i in range(0,len(d)):
    w=list(d[i])
    for j in range(0,len(w)):
        print(int(w[j]),end="")
    print("\r")
