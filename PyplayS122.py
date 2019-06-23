import calendar
n=list(map(int,input().split("-")))
l=list(calendar.month_name)
print(l[int(n[1])])
