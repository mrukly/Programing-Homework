import turtle

x1_1, y1_1 = map(int, input().split())
x1_2, y1_2 = map(int, input().split())

x2_1, y2_1 = map(int, input().split())
x2_2, y2_2 = map(int, input().split())

l1 = min(x1_1, x1_2)
r1 = max(x1_1, x1_2)
t1 = max(y1_1, y1_2)
b1 = min(y1_1, y1_2)

l2 = min(x2_1, x2_2)
r2 = max(x2_1, x2_2)
t2 = max(y2_1, y2_2)
b2 = min(y2_1, y2_2)

if (r1 < l2 or r2 < l1 or t1 < b2 or t2 < b1):
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif (r1 == l2 or r2 == l1 or t1 == b2 or t2 == b1):
    print("Прямоугольники имеют касание")
elif (l1 >= l2 and r1 <= r2 and b1 >= b2 and t1 <= t2) or \
     (l2 >= l1 and r2 <= r1 and b2 >= b1 and t2 <= t1):
    print("Один прямоугольник лежит внутри другого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")

m = 10

turtle.penup()
turtle.goto(l1 *10, b1 * 10)
turtle.pendown()
for _ in range(2):
    turtle.forward((r1 - l1) * m)
    turtle.left(90)
    turtle.forward((t1 - b1) * m)
    turtle.left(90)

turtle.penup()
turtle.goto(l2 * m, b2 * m)
turtle.pendown()
for _ in range(2):
    turtle.forward((r2 - l2) * m)
    turtle.left(90)
    turtle.forward((t2 - b2) * m)
    turtle.left(90)

turtle.done()
