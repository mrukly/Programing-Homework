import turtle

x1_1, y1_1 = map(int, input().split())
x1_2, y1_2 = map(int, input().split())

# Ввод данных для второго прямоугольника
x2_1, y2_1 = map(int, input().split())
x2_2, y2_2 = map(int, input().split())

if x1_2 < x2_1 or x2_2 < x1_1 or y1_1 > y2_2 or y2_1 > y1_2:
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif x1_2 == x2_1 or x2_2 == x1_1 or y1_1 == y2_2 or y2_1 == y1_2:
    print("Прямоугольники имеют касание")
elif (x1_1 <= x2_1 and x1_2 >= x2_2 and y1_1 >= y2_1 and y1_2 <= y2_2) or \
     (x2_1 <= x1_1 and x2_2 >= x1_2 and y2_1 >= y1_1 and y2_2 <= y1_2):
    print("Один прямоугольник лежит внутри другого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")

turtle.penup()
turtle.goto(x1_1, y1_1)
turtle.pendown()
for _ in range(2):
    turtle.forward(x1_2 - x1_1)
    turtle.right(90)
    turtle.forward(y1_1 - y1_2)
    turtle.right(90)

turtle.penup()
turtle.goto(x2_1, y2_1)
turtle.pendown()
for _ in range(2):
    turtle.forward(x2_2 - x2_1)
    turtle.right(90)
    turtle.forward(y2_1 - y2_2)
    turtle.right(90)

turtle.done()
