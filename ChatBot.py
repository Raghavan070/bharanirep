def bot(a):
    print(a)
    m=[]
    c=[]
    s=str(input("Enter your name "))
    m.append(s)
    x=1
    a=int(input("Do u want to book room?? (Enter '0' to book) "))
    if a==0:
        b=int(input("How many room you want to book "))
        m.append(b)
        c=list(map(str,input("What do u like have?? ").split()))
        print("Hi",m[0],"you have booked",m[1],"rooms and ordered",end=" ")
        for i in range(0,len(c)):
            if len(c)==1:
                print(c[i],"/r")
            elif len(c)==0:
                print("nothing/r")
            elif i!=(len(c)-1):
                print(c[i],end=",")
            else:
                print("and",c[i])
        s=str(input("Enter your suggesions "))

x=str(input())
try:
    if x!=" ":
        bot(x)
        print("Thankyou...visit again")
finally:
    print("")
