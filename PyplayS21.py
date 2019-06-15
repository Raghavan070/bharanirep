d=[]
for i in range(3):
    p=list(input().split())
    d.append(p)
if d[0][0]==d[1][0] and d[2][0]==d[1][0]: print("yes")
elif d[0][1]==d[1][1] and d[2][1]==d[1][1]: print("yes")
else: print("no")
