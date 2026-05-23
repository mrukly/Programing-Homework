def check(sms):
    """
    Returns the full message if length < 160, otherwise returns first 160 characters

    Parameters:
    sms (str): The input message

    Returns:
    str: Valid message
    """
    if len(sms) <= 160:
        return sms
    else:
        return sms[:160]

text = input("Введите сообщение: ")
print(check(text))
