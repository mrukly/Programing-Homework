from math import ceil

n, k, m = map(int, input().split())

q = ceil(n * 2 / k)
t = q * m

print(t)
