def count_chars(s):
    v = 0
    c = 0
    
    vowels = "аеёиоуыэюяaeiouy"
    consonants = "бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxz"
    
    s = s.lower()
    
    for ch in s:
        if ch in vowels:
            v += 1
        elif ch in consonants:
            c += 1
    
    print("Гласных:", v)
    print("Согласных:", c)

phrase = input()
count_chars(phrase)
