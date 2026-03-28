def check(sms):
    if len(sms) <= 160:
        return sms
    else:
        return sms[:160]

text = input("Введите сообщение: ")
print(check(text))
