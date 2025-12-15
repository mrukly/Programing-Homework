n, k, r = map(int, input().split())
s = 0

while n < r * (1 + k / 100):
    n *= (1 + k/100)
    s += 1
print(s)
