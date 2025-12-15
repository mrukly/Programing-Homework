n = int(input())

while n > 0 and n % 2 == 0:
    n //= 2
if n == 1:
    print("Верно")
else:
    print("Неверно")
