weight = float(input()) 
height = float(input()) 

bmi = (weight / (height * height)) * (0.453592 / (0.0254 ** 2))

print(round(bmi, 2))
