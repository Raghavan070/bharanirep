def c(n): 
    if n <=1 : 
        return 1
    s = 0 
    for i in range(n): 
        s += c(i) * c(n-i-1)
    return s 
  
n=int(input())
l=[]
for i in range(n): 
    l.append(c(i))
print(*l)
