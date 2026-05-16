s = input()

words = s.split()

for word in words:
    if words.count(word) == 2:
        print(word)
        break
