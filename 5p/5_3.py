n = int(input())

first = n // 1000
second = (n // 100) % 10
third = (n // 10) % 10
fourth = n % 10

if first == fourst and second == third:
    print("настоящее")
else:
    print("кривое")
