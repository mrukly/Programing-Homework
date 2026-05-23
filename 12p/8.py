def fib(k):
    """
    Calculates the k-th Fibonacci number

    Parameters:
    k (int): The position in the Fibonacci sequence (k >= 0)

    Returns:
    int: The k-th Fibonacci number
    """
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

k = int(input())
print(fib(k))
