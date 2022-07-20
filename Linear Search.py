l = [3,5,10,12,15,28,35,60]
item = 10
f = 0
e = len(l) - 1
m = (f+e) // 2
if l[m] == item:
    print(l[m])
elif l[m] < item:
    print(l[m+1])
else:
    print(l[m-1])