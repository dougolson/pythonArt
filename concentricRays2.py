import random
import turtle
import math

# Draws three sets of concentric rays with a sort of spiral galaxy effect.
# Small step size and multiple nested loops runs quite slowly. Probably not the most efficient code.

def colorGen(sat = 1, val = 1):
    "Generates random RGB values. sat range 0-1, val range = 0-1"
    rand1 = round(random.randrange(256)*val)
    rand2 = round(random.randrange(256)*val)
    sat2 = round((1-sat)*255)
    if rand1 >= rand2:
        rand1 = round(255*val)
    else:
        rand2 = round(255*val)
    color = [[sat2, rand1, rand2], [rand1, sat2, rand2], [sat2, rand2, rand1],
             [rand1, rand2, sat2], [rand2, sat2, rand1], [rand2, rand1, sat2]]
    return tuple(color[random.randrange(6)])

def timeTunnel(repeats = 1,zigzag = 10, stepVar = 1, curve = 0):
    "Draws fuzzy concentric circles. zigzag is sd of randomgauss, stepVar is sd of length, curve is a multiplier that gives a spiral effect"
    for i in range(repeats):
        alex.goto(0,0)
        alex.seth(random.uniform(0,360)) # set heading
        h1 = alex.heading() # get heading
        alex.color(colorGen(val=0))
        for j in range(50):
            alex.down()
            alex.forward(abs(round(random.gauss(2, stepVar),0))) # abs limits motion to forward
            alex.seth(h1 + curve*j + random.gauss(0,4*zigzag))
            x = alex.xcor()
            y = alex.ycor()
            alex.color(colorGen(val = j/50))
            h2 = alex.heading()
        for k in range(2):
            alex.down()
            alex.seth(h2)
            for k2 in range(50):
                alex.color(colorGen(val = k2/50))
                alex.seth(h2 + curve*k2 + random.gauss(0,2*zigzag))
                alex.forward(abs(round(random.gauss(2, stepVar), 0)))
            alex.up()
            m = alex.xcor()
            n = alex.ycor()
            h3 = alex.heading()
            # h4 = alex.heading()
            for l in range(4):
                alex.color(colorGen())
                alex.down()
                alex.seth(h3)
                # h5 = alex.heading()
                for l2 in range(50):
                    alex.color(colorGen(val = l2/50))
                    alex.seth(h3 + curve*l2 + random.gauss(0,zigzag))
                    alex.forward(abs(round(random.gauss(2,stepVar),0)))
                alex.up()
                alex.goto(m, n)
            alex.goto(x, y)
        alex.up()

turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(255)
turtle.bgcolor("black")
alex = turtle.Turtle()
alex.speed(10)
alex.pensize(0)
alex.ht()

timeTunnel(1000,1, 1, .5)

turtle.update()
wn.exitonclick()
