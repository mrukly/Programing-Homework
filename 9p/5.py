try:
    with open('input.txt', 'r', encoding='utf-8') as file1:
        a, b, c = map(int, file1.read().split())
    
    result = a / b + c
    
    with open('output.txt', 'w', encoding='utf-8') as file2:
        file2.write(result)
        
except ValueError:
    with open('output.txt', 'w', encoding='utf-8') as file1:
        file2.write("ValueError")
        
except ZeroDivisionError:
    with open('output.txt', 'w', encoding='utf-8') as file1:
        file2.write("ZeroDivisionError:")
