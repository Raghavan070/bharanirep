import sys
n=list(map(int,input()))
s=0
n=n[::-1]
for i in range(0,len(n)):
    s=s+(n[i]*(2**i))
for i in range(0,s+100):
    if 2**i==s:
        print(2**(i-1))
        sys.exit()
    elif 2**i>s:
        print(2**i)
        sys.exit()
