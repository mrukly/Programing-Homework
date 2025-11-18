weight = float(input()) 
height = float(input()) 

bmi = (weight / (height * height)) * (0.453592 / (0.0254 ** 2))
bmi= round(bmi, 2)

if bmi < 16:
    print("выраженный дефицит массы тела")
elif 16 <= bmi < 18.5:
    print("недостаточная масса тела")
elif 18.5 <= bmi < 25:
    print("норма")
elif 25 <= bmi < 30:
    print("избыточная масса тела")
elif 30 <= bmi < 35:
    print("ожирение первой степени")
elif 35 <= bmi < 40:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")
