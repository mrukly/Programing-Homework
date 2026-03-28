def seconds(s):
    m = int(s[:2])
    d = int(s[3:5])
    y = int(s[6:10])
    h = int(s[11:13])
    mn = int(s[14:16])
    sc = int(s[17:19])
    
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        mon[1] = 29
    
    days = sum(mon[:m-1]) + d - 1
    
    return days * 86400 + h * 3600 + mn * 60 + sc

date = input("Введите дату и время (MM/DD/YYYY HH:MM:SS): ")
print(seconds(date))
