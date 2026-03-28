def card(price):
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
