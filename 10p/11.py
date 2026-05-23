def check(n):
    """
    Returns True if n is a prime number, otherwise returns False

    Parameters:
    n (int): Number to check

    Returns:
    bool: True if prime, False otherwise
    """
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())

for i in range(1, N + 1):
    if check(i):
        print(i, end=" ")
