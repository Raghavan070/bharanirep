n=int(input()) 
k=list(map(int, input ().split())) 
m=100000 
for i in range(n): 
    if k.count(n[i])<m: m=n[i] 
print(m)
