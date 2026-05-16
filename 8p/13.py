n = 1
while True:
    s = input()
    if len(s) % 2 == 0:
        half = len(s) // 2
        left_sum = 0
        right_sum = 0
        for i in range(half):
            left_sum += int(s[i])
            right_sum += int(s[i + half])
        if left_sum == right_sum:
            print(n)
            break
    n += 1
