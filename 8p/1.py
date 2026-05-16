text = input()

max_sp = 0
cur_sp = 0

for i in text:
    if i.isspace():  
        cur_sp += 1
        if cur_sp > max_sp:
            max_sp = cur_sp
    else:
        cur_sp = 0

print(max_sp)
