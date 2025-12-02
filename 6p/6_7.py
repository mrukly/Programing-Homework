k = int(input())

c = 0

for a in range(k // 5 + 1):
    for b in range(k // 7 + 1):
        if 5 * a + 7 * b == k:
            c = 1
            break
    if c == 1:
        break

if c == 1:
    print('да')
else:
    print('нет')
