s = input()

words = s.split()
min_len = len(words[0])

for word in words[1:]:
    if len(word) < min_len:
        min_len = len(word)

print(min_len)
