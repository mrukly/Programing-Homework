import math

a = int(input())
b = int(input())
c = int(input())

A = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c)))
B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
C = math.degrees(math.pi - A - B)

print(A)
print(B)
print(C)
