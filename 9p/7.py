with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
for i in lines:
    line = i.strip()
    if line and int(line) != 100:
        result.append(i)

with open('input.txt', 'w', encoding='utf-8') as f:
    f.writelines(remaining_lines)
