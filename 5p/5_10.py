n = int(input())

a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10

if n < 1000 or n > 9999:
    print("ERROR")
elif a == b or a == c or a == d or b == c or b == d or c == d:
    print("ERROR")
elif 1900 <= n <= 2050:
    print("ERROR")
else:
    print("OK")
