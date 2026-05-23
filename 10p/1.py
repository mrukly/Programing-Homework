def count_chars(s):
    """
    Counts the number of vowels and consonants in a sentence

    Parameters:
    s (str): A sentence in Russian

    Returns:
    None
    """
    
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
