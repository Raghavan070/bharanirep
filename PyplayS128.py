n=int(input())
l=list(map(int,input().split()))
if n==1:
    if n%2==0: print("even")
    else: print("odd")
else:
    if l[0]%2==0 and l[1]%2==0: print("even")
    else: print("no")
