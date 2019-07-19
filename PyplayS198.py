n=int(input()) 
k=list(map(int, input ().split())) 
print(abs(k.index(max(k))-k.index(min(k))))
