import sys
n=int(input())
l=list(map(int,input().split()))
s=0
if n==1:
    print(1)
    sys.exit()
for i in range(1,n-1):
    if (l[i]<l[i-1] and l[i]<l[x]) or (l[i]>l[i-1] and l[i]>l[x]): s=s+1
print(s)
