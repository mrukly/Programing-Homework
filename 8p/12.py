import keyword

name = input()

if name.isidentifier() and not keyword.iskeyword(name):
    print("Может быть именем")
else:
    print("Не может быть именем")
