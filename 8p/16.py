text = input()
check = 0
answer = True
for i in text:
    if i == '(':
        check += 1
    elif i == ')':
        check -= 1
        if check < 0:
            answer = False
            break

if answer and check == 0:
    print("Правильно")
else:
    print("Неправильно")
