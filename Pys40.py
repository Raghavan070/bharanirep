n=int(input())

a=1
b=1
if(n==1):
    print(a,end='')
count=0
if(n>1):
    while(count<n):
        if(count==n-1):
            print(a,end='')
        else:
            print(a,end=' ')
        nh=a+b
        a=b
        b=nh
        count=count+1
