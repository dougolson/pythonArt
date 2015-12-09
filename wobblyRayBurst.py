import turtle
import random

# Draws a burst of wobbly rays with multicolored scribbles on the ends

turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(255)
turtle.bgcolor("black")
alex = turtle.Turtle()
alex.speed(10)
alex.goto(0,0)
alex.pensize(0)
alex.ht()
for i in range(1000):
    alex.goto(0,0)
    alex.seth(random.uniform(0,360))
    h = alex.heading()
    alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
    for j in range(20):
        alex.down()
        alex.forward(abs(round(random.gauss(0,15),0)))
        alex.seth(h + random.uniform(0,60))
        x = alex.xcor()
        y = alex.ycor()
    for k in range(13):
        alex.up()
        s = round(random.gauss(0,5), 0)
        t = round(random.gauss(0,5), 0)
        alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
        alex.pensize(0)
        alex.goto(x + s, y + t)
        alex.down()
        u = round(random.gauss(0,10), 0)
        v = round(random.gauss(0,10), 0)
        alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
        alex.pensize(0)
        alex.goto(x + u, y + v)
    alex.up()
turtle.update()
wn.exitonclick()
