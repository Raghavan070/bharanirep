n=int(input())
l=list(map(int,input().split()))
u,v=map(int,input().split())
print(abs(l.index(u)-l.index(v)))
