def multiples(a, b, n):
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            print(i)

a = int(input("A: "))
b = int(input("B: "))
n = int(input("N: "))

multiples(a, b, n)
