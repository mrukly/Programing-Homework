x, y = map(int, input().split())

a = int(x % y == 0 or y % x == 0)

print(a)
