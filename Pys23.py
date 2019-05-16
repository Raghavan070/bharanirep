n=int(input())
if n==2 or n==3 or n==5 or n==7:
    print("yes")
elif(n%2==0) or(n%3==0) or (n%5==0) or (n%7==0) or (n==1) or n<0:
    print("no")
else:
    print("yes")
