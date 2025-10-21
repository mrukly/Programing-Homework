a1 = input('Собака короткошерстной породы? ')

if a1.lower == 'да':
  a2 = input('Рост собаки менее 50 см? ')
  if a2.lower == 'да':
    a3 = input('У собаки короткий хвост? ')
    if a3.lower == 'да':
      print('Английский бульдог')
    else:
      a4 = input('У собаки длинные уши')
      if a4.lower == 'да':
        print('Гончая')
      else:
        a5 = input('У собаки короткое тело? ')
        if a5.lower == 'да':
          print('Мопс')
        else:
          print('Чихуахуа')
  else:
    a3 = input('Собака весит более 50 кг? ')
    if a3.lower == 'да':
      print('Датский дог')
    else:
      print('Фоксхаунд')
else:
  a2.lower = input('Рост собаки менее 50 см? ')
  if a2.lower == 'да':
    a3 = input('У собаки доброжелательный характер? ')
    if a3.lower == 'да':
      print('Кокер-спаниэль')
    else:
      print('Ирландский сеттер')
  else:
    a3 = input('Рост собаки менее 70см? ')
