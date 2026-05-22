with open('input.txt', 'r', encoding='utf-8') as file1:
    lines = file1.readlines()

if not lines[0].strip().isdigit():
    result = "ERROR"
else:
    n = int(lines[0].strip())
    result = "YES" if len(lines) - 1 == n else "NO"

with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.write(result)
