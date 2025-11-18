import turtle

xc = int(input(xc = ))
yc = int(input(yc = ))
r = int(input(r = ))
x = int(input(x = ))
y = int(input(y = ))

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)
t.penup()
t.goto(x, y)
t.pendown()
t.dot(5)

p = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5

if abs(p - r) < 0.001:
    print("на окружности")
elif abs(p) < r:
    print("внутри окружности")
else:
    print("за пределами окружности")

turtle.done()
