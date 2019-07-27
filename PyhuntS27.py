# your code goes here 
n=list(input())
if n!=n[::-1]: print("".join(n)) 
else: print ("".join(n[0:len(n)-1])) 
