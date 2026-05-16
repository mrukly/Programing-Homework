def sortstr(s):
    chars = list(s)           
    chars.sort()              
    return ''.join(chars)    

s = input()
print(sortstr(s))
