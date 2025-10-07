X, Y, N = map(int, input().split())

C = (X * 100 + Y) * N
K = C % 100
R = (C - K) / 100

print(R, 'руб.', K, 'коп.')
