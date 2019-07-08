n=list(map(str,input()))
k=list(map(str,input()))
for i in range(len(k)):
    n.append(k[i])
if len(set(n))==26: print("complementary")
else: print("non-complementary")
