a = input()
b = input()
c = input()

result = ""

for i in a + b + c:
    if i in result:
        continue
    
    in_a = i in a
    in_b = i in b
    in_c = i in c
    
    if in_a + in_b + in_c == 1:
        result += i

print(result)
