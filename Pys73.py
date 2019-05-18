s=list(map(int,input().split()))
for i in range(0,len(s)-2):
    for j in range(0,len(s)-2-i):
        if s[j] > s[j + 1]:
            k=s[j]
            s[j]=s[j+1]
            s[j+1]=k
print(s[0])
