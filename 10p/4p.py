def make_payment(P):
    """
    Checks if a credit card payment is valid

    Parameters:
    P (float): The payment amount attempted

    Returns:
    None
    """
    
    limit = 1000
    minimal = 20
    
    if P >= minimal and P <= limit:
        print("Успех")
    else:
        print("Повторить попытку")

n = float(input("Введите сумму платежа: "))
make_payment(n)
