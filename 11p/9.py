# input
print("Введите текст (пустая строка для завершения):")
text = ""
while True:
    line = input()
    if line == "":
        break
    text += line + " "

# cleaning
clean_text = ''
for c in text:
    if c.isalpha() or c == ' ' or c == "'":
        clean_text += c.lower()
    else:
        clean_text += ' '

words = clean_text.split()

# count
word_count = {}
order = []

for word in words:
    if word not in word_count:
        word_count[word] = 1
        order.append(word)
    else:
        word_count[word] += 1

# sorting
for i in range(len(order)):
    for j in range(len(order) - 1):
        if word_count[order[j]] < word_count[order[j + 1]]:
            order[j], order[j + 1] = order[j + 1], order[j]

# result
for word in order:
    print(word)
