import sys
n=input()
for i in range(0,len(n)):
    for j in range(len(n)-1,i,-1):
        if n[i]==n[j]:
            x=n[i:j+1]
            if x==x[::-1]:
                print(x)
                sys.exit()
