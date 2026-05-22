with open('input.txt', 'r', encoding='utf-8') as file1:
    lines = file1.readlines()

result = []
for i in lines:
    line = i.rstrip('\n')
    if len(line) > 20:
        result.append(i)

with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(result)
