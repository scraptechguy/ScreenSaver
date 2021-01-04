import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)


square = turtle.Turtle()
square.speed(0)
square.shape("square")
square.color("red")
square.penup()
square.goto(0, 0)
square.dx = 0.1
square.dy = 0.1

while True:

    wn.update()

    square.setx(square.xcor() + square.dx)
    square.sety(square.ycor() + square.dy)

    if square.ycor() > 350:
        square.sety(350)
        square.dy *= -1

    if square.ycor() < -350:
        square.sety(-350)
        square.dy *= -1

    if square.xcor() > 630:
        square.setx(630)
        square.dx *= -1

    if square.xcor() < -630:
        square.setx(-630)
        square.dx *= -1
