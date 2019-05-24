
a,b=map(int, input (). split ()) 
c,d=map(int, input (). split ()) 
e,f=map(int, input (). split ()) 
g,h=map(int, input (). split ()) 
m=abs(a-b)
n=abs(c-d)
o=abs(e-f)
p=abs(g-h)
w=[] 
w.append(m)
w.append(n)
w.append(o)
w.append(p)
if len(set(w))==2:
	print ("yes")
else:
    print ("no")
