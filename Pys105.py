p,t,r=map(float,input().split())
r1=r/100
x=p*(1+(t*r1))
m=abs(p-x)
print(int(m))
