def sum_progress(a1, r, n):
    """
    Calculates the sum of the first n terms of an arithmetic progression

    Parameters:
    a1 (float): The first term of the progression
    r (float): The common difference
    n (int): The number of terms to sum (n >= 1)

    Returns:
    float: The sum of the first n terms
    """
    if n == 1:
        return a1
    else:
        return sum_progress(a1, r, n - 1) + a1 + (n - 1) * r


a1 = float(input())
r = float(input())
n = int(input())

result = sum_progress(a1, r, n)
print(result)
