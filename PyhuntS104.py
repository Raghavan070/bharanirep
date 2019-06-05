from itertools import accumulate
n=list(map(int,input()))
m=list(accumulate(n))
s=0
for i in range(0,len(m)):
    s=s+m[i]
print(s)
