n = input()
a = ord(n[0]) - ord('a') + 1
b = int(n[1])

if (a + b) % 2 == 0:
    print('черный')
else:
    print('белый')
