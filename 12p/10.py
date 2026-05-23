def maxlist(a):
    """
    Finds the maximum element in a list of integers

    Parameters:
    a (list): A list of integers (non-empty)

    Returns:
    int: The maximum element in the list
    """
    rest = maxlist(a[1:])
    first = a[0]
    
    if firstt > rest:
        return first
    else:
        return rest


numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

print(maxlist(numbers))
