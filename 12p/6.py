def degree5(n):
    """
    Check if n is a power of 5 and returns the exponent

    Parameters:
    n (int): The natural number to check

    Returns:
    int: The exponent k such that 5^k = n, or -1 if n is not a power of 5
    """
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    result = degree5(n // 5)
    if result != -1:
        return result + 1
    return -1

n = int(input())
print(degree5(n))
