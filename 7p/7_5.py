n = int(input())
answer = []
i = 1

while i ** 3 <= n:
    answer.append(i ** 3)
    i += 1
    
print(' '.join(map(str, answer)))
