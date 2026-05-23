def valid(A, B):
    """
    Prints numbers between A and B (inclusive) whose digits are only from {1,3,4,8,9}

    Parameters:
    A (int): Start of the range
    B (int): End of the range

    Returns:
    None
    """
    
    if A > B:
        A, B = B, A
    for i in range(A, B + 1):
        for c in str(i):
            if c not in "13489":
                break
        else:
            print(i, end=" ")

a = int(input("A: "))
b = int(input("B: "))
valid(a, b)
