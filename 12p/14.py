def numbers(x):
    """
    Prints digits of a natural number x in reverse order
    Prints one digit per line

    Parameters:
    x (int): A natural number (x >= 1)
    """
    print(x % 10)
    
    if x > 9:
        numbers(x // 10)

x = int(input())

numbers(x)
