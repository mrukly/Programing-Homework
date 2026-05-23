def count(n):
    """
    Counts the number of digits in a natural number.

    Parameters:
    n (int): A natural number (n >= 1).

    Returns:
    int: The number of digits in n.
    """
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)

n = int(input())
result = count(n)
print(result)
