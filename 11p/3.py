s = input("Введите предложение: ")

clean = ''
for c in s:
    if c.isalpha() or c == ' ':
        clean += c
    else:
        clean += ' '

words = clean.split()
print(words)
