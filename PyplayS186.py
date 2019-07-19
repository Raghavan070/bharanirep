s=list(input())
a=b=0
for i in range(len(s)-5):
    q="".join(s[i:i+6])
    if q=="Vishal": a=1
    if q=="Sundar": b=2
if a==1 and b==2: print("yes")
else: print("no")
