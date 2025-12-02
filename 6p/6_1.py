import math

D = 2 * 6.5

A = int(input())
B = int(input())

d = math.sqrt(A**2 + B**2)
if d <= D: 
    print("да")
else:
    print("нет")
