def card(price):
    """
    Returns the total value of a phone card including bonuses

    Parameters:
    price (int): Price of the card

    Returns:
    int: Total value including bonus, or -1 if the price is invalid
    """
    if price == 5 or price == 10:
        final = price
    elif price == 25:
        final = price + 3
    elif price == 50:
        final = price + 8
    elif price == 100:
        final = price + 20
    else:
        print("Ошибка")
        return
    
    print(final)

p = float(input())
card(p)
