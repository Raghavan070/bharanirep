n=list(input().split())
s=0
q = list(n[0])
w = list(n[1])
for i in range(0,min(len(q),len(w))):
    if q[i]!=w[i]: s=s+1
s=s+(len(q)-len(w))
if s==int(n[2]): print("yes")
else: print("no")
