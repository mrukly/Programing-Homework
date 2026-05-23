def convert(s):
    """
    Converts date and time from 'MM/DD/YYYY HH:MM:SS' to 'DD.MM.YY HH:MM:SS AM/PM'

    Parameters:
    s (str): Input string in format 'MM/DD/YYYY HH:MM:SS'

    Returns:
    None
    """
    m = int(s[:2])
    d = int(s[3:5])
    y = s[6:10]
    h = int(s[11:13])
    mn = s[14:16]
    sc = s[17:19]
    
    if m < 1 or m > 12 or h < 0 or h > 23:
        print("Ошибка")
        return
    
    ap = "AM" if h < 12 else "PM"
    h12 = 12 if h % 12 == 0 else h % 12
    
    print(f"{d:02d}.{m:02d}.{y[2:]} {h12}:{mn}:{sc} {ap}")

date = input("Введите дату и время (MM/DD/YYYY HH:MM:SS): ")
convert(date)
