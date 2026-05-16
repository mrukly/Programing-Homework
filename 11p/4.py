s = input("Введите предложение: ")

clean = ''
for c in s:
    if c.isalpha() or c == ' ':
        clean += c
    else:
        clean += ' '

words = clean.split()

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(unique_words)
