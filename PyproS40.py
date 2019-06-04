from itertools import permutations
a="dhoni"
s=0
b=list(map(str,input()))
lv=list(permutations(str(a),len(a)))
for i in range(0,len(lv)):
    if b==list(lv[i]):
        s=1
        print("yes")
        break
if s==0: print("no")
