def fibonacci(n): 
    a, b = 1, 1
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

N = int(input("Введите количество чисел Фибоначчи: "))
fibonacci(N)
