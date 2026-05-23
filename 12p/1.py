def pownum(a, n):
    """
    Raises a real number a to a natural power n

    Parameters:
    a (float): The base number (real number)
    n (int): The exponent (natural number, n >= 1)

    Returns:
    float: a raised to the power n
    """
    if n == 1:
        return a
    else:
        return a * pownum(a, n - 1)

a = float(input())
n = int(input())

print(pownum(a, n))
