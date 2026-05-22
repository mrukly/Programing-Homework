with open('input.txt', 'r', encoding='utf-8') as file1:
    lines = file1.readlines()

chars = []
for i in lines:
    if i.strip():  
        chars.append(i[0])

result = ''.join(chars)

with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.write(result)
