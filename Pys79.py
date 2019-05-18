m,n=map(int,(input().split()))
s=abs(m-n)
x=s%2
if x==0:
    print("even")
else:
    print("odd")
