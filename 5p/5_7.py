N, K, M = map(int, input().split())

if M > K:
    a = M - K - 1
else:
    a = N - K + M - 1

if M < K:
    b = K - M - 1
else:
    b = K + N - M - 1

if a < b:
    print(a)
else:
    print(b)
