import sys
n=int(input())
l=[]
for i in range(0,n):
    d=input()
    l.append(d)
for i  in range(0,n-1):
    if l[i]==l[i+1]:
        print("yes")
        sys.exit()
print("no")
