with open('input.txt', 'r', encoding='utf-8') as file1:
    lines = file1.readlines()

result = []
for i in lines:
    if i and i[0] == 'A':  
        result.append(i)

with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(result)
