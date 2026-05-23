def progress(a1, r, n):
    """
    Finds the n-th term of an arithmetic progression

    Parameters:
    a1 (float): The first term of the progression
    r (float): The common difference
    n (int): The position of the term to find (n >= 1)

    Returns:
    float: The n-th term of the arithmetic progression
    """
    if n == 1:
        return a1
    else:
        return progress(a1, r, n - 1) + r


a1 = float(input())
r = float(input())
n = int(input())

print(progress(a1, r, n))
