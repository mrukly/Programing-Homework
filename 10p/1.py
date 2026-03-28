def count_chars(s):
    vowels = set('аеёиоуыэюя')
    cons = set('бвгджзйклмнпрстфхцчшщъь')
    
    v = 0
    c = 0
    
    s = s.lower()
    
    for ch in s:
        if ch in vowels:
            v += 1
        elif ch in cons:
            c += 1
    
    print("Гласных:", v)
    print("Согласных:", c)

phrase = input()
count_chars(phrase)
