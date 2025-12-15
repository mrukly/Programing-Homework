answer = []

for i in range(100, 1000):
    if i % 17 == 0:
        answer.append(i)

print(' '.join(map(str, answer)))
print(len(answer))
