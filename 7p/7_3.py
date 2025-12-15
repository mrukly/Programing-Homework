import math

n = int(input())
sn = math.sqrt(n)

while sn % 1 != 0:
    print("Не является полным квадратом")
    n = int(input())
    sn = math.sqrt(n)
print("Является полным квадратом")
