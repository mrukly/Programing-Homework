s = 0
t1 = float(input())

while t1 != 0:
    t2 = float(input()) 
    if t2 == 0:
        break
    if t2 < t1:
        s += 1
    t1 = t2
print(s)
