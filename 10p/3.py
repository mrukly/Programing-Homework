def price(price, card, holiday):
    """
    Calculates the final price after applying discounts

    Parameters:
    price (float): Purchase price
    card (bool): True if the customer has a discount card
    holiday (bool): True if it is a holiday

    Returns:
    float: Final price after applying all discounts
    """
    
    price = round(price, 2)
    
    discount = 0
    
    if price > 30000:
        discount += 10
    elif price > 20000:
        discount += 7
    elif price > 15000:
        discount += 5
    elif price > 5000:
        discount += 3
    
    if card:
        discount += 5
    
    if holiday:
        discount += 3
    
    if discount > 15:
        discount = 15
    
    price = price * (100 - discount) / 100
    
    price = round(price, 2)
    
    return price

p = float(input("Стоимость: "))
c = input("Есть ли карта?: ").lower() == "да"
h = input("Сегодня праздник? ").lower() == "да"

print(price(p, c, h))
