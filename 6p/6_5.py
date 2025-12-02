n = input()
x1 = ord(n[0]) - ord('a') + 1
y1 = int(n[1])
x2 = ord(n[3]) - ord('a') + 1
y2 = int(n[4])

a = abs(x1 - x2)
b = abs(y1 - y2)

if (a == 1 and b == 2) or (a == 2 and b == 1):
    print('верно')
else:
    print('ошибка')
