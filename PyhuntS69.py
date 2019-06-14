n=list(input())
x=['.','c','o','m'] 
y=['g','m','a','i','l']
if n.count('@')==1 and n.count('.')==1 and len(n[n.index('@'):n.index('.')])>=4 and len(n[0:n.index('@')])>=3 and (n[len(n)-4:len(n)])==x and (n[n.index('@')+1:n.index('.')])==y:
    print("YES")
else: print("NO")
