m=list(map(int,input().split("/")))
if 0<m[0]<32 and 0<m[1]<13 and m[2]>1300 and len(m)==3: print("yes")
else: print("no")
