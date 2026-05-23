def multiples(a, b, n):
    """
    Prints all common multiples of A and B up to N in ascending order

    Parameters:
    a (int): First natural number
    b (int): Second natural number
    n (int): Upper limit

    Returns:
    None
    """
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            print(i)

a = int(input("A: "))
b = int(input("B: "))
n = int(input("N: "))

multiples(a, b, n)
