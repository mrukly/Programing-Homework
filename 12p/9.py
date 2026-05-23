def combin(n, k):
    """
    Calculates the binomial coefficient C(n, k)

    Parameters:
    n (int): Total number of elements (n >= 0)
    k (int): Number of chosen elements (0 <= k <= n)

    Returns:
    int: The binomial coefficient C(n, k)
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)

n = int(input())
k = int(input())

print(combin(n, k))
