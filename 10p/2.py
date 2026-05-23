def fibonacci(n): 
    """
    Prints the first N numbers of the Fibonacci sequence

    Parameters:
    n (int): The number of Fibonacci numbers to print (n >= 1)

    Returns:
    None
    """
    
    a, b = 1, 1
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

N = int(input("Введите количество чисел Фибоначчи: "))
fibonacci(N)
