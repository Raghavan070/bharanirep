n=list(input())
s=0
for i in range(len(n)-1,-1,-1): s=s+((2**i)*int(n[i]))
print(s)
