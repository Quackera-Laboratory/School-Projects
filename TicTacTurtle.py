import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(1)
turtle.colormode(255)
t.color((75, 41, 183))

for turn in range(10):
    t.forward(150)
    t.backward(85)
    t.right(90)
    t.forward(85)
    t.left(180)
    t.forward(150)
