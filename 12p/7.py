def nod(a, b):
    """
    Calculates the greatest common divisor of two natural numbers

    Parameters:
    a (int): First natural number
    b (int): Second natural number

    Returns:
    int: The greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return nod(b, a % b)

a = int(input())
b = int(input())

result = nod(a, b)
print(result)
