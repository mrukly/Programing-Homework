text = input()

max_count = 1
cur_count = 1

for i in range(1, len(text)):
  if text[i] == text[i - 1]:
    cur_count += 1
    if cur_count > max_count:
      max_count = cur_count
    else:
      cur_count = 1
print(max_coun)
