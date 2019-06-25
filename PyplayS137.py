n=int(input())
n=list(bin(n))
n=n[::-1]
print(n.index("1")+1)
