n=list(input())
x=['.','c','o','m']
if n.count('@')==1 and n.count('.')==1 and len(n[n.index('@'):n.index('.')])>=4 and len(n[0:n.index('@')])>=3 and (n[len(n)-4:len(n)])==x:
    print("YES")
else: print("NO")
