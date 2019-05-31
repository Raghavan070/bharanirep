from itertools import combinations
a,b=map(int,input().split())
h=len(str(a))
lv=list(combinations(str(a),h-b))
lv=(sorted(lv))
x="".join(lv[0])
print(x)
