import math
import turtle

x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())

turtle.penup()
turtle.goto(x1 * scale, y1 * scale - r1 * scale)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2 * scale, y2 * scale - r2 * scale)
turtle.pendown()
turtle.circle(r2)

turtle.done()

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d > r1 + r2:
    print("Окружности лежат одна вне другой, не касаясь")
elif d == r1 + r2:
    print("Окружности имеют внешнее касание")
elif d > abs(r1 - r2) and d < r1 + r2:
    print("Окружности пересекаются")
elif d == abs(r1 - r2) and d != 0:
    print("Окружности имеют внутреннее касание")
elif d < abs(r1 - r2):
    print("Одна окружность лежит внутри другой, не касаясь")
else:  # d == 0 and r1 == r2
    print("Окружности совпадают")

