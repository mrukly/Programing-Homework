with open('input.txt', 'r', encoding='utf-8') as file1:
    data = file1.read()

result = data.upper()

with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.write(result)
