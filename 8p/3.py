text = input().lower()
unique = ""

for i in text:
    if i not in unique:
        unique += i

print(len(unique))
