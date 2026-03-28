def make_payment(P):
    limit = 1000
    minimal = 20
    
    if P >= minimal and P <= limit:
        print("Успех")
    else:
        print("Повторить попытку")

n = float(input("Введите сумму платежа: "))
make_payment(n)
