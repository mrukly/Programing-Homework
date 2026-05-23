def mod_number(a, b):
    """
    Finds the remainder when dividing natural number a by natural number b

    Parameters:
    a (int): The dividend (natural number, a >= 0)
    b (int): The divisor (natural number, b >= 1)

    Returns:
    int: The remainder of a divided by b
    """
    if a < b:
        return a
    else:
        return mod_number(a - b, b)


a = int(input())
b = int(input())

print(mod_number(a, b))
