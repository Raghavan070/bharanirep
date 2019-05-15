def fac(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
    
d=int(input("Enter depth"))
k=2*d-2
for i in range(0,d):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print(int((fac(i)/(fac(j)*fac(i-j))))," ",end="")
    print("\n")
