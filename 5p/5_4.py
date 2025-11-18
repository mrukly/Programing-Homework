n = int(input())

m = n % 10

if 11 <= n <= 14:
    print(n, "попугаев")
elif m == 1:
    print(n, "попугай")
elif 2 <= m <= 4:
    print(n, "попугая")
else:
    print(n, "попугаев")
