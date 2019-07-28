import sys
n,k=map(int,input().split())
if len(list(str(n)))>7:
    print(int(str(n)+(str('0')*k)))
    sys.exit()
for i in range(1,n+1):
    if int(str(i)+(str('0')*k))%n==0:
        print(int(str(i)+(str('0')*k)))
        sys.exit()
