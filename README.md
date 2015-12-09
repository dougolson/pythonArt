<img align="left" src="rainbowGalaxy.png" height="100" width="100">
###A series of images made with Python Turtle Graphics

I've been playing around with turtle graphics - it's a fun way to learn, and with a little experimentation and thought you can come up with all sorts of interesting images.

The first image is pretty simple:

	import turtle
	import random
	# Draws a burst of straight rays, uses a nested loop to make small
	# scribbles at the end of each ray
	turtle.tracer(0, 0)
	wn = turtle.Screen()
	wn.colormode(255)
	turtle.bgcolor("black")
	alex = turtle.Turtle()
	alex.speed(10)
	alex.goto(0,0)
	alex.pensize(0)
	alex.ht()
	for i in range(400):
	    alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
	    alex.goto(round(random.gauss(0,100),0),round(random.gauss(0,100),0))
	    x = alex.xcor()
	    y = alex.ycor()
	    for j in range(25):
	                s = round(random.gauss(0,5), 0)
	                t = round(random.gauss(0,5), 0)
	                alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
	                alex.pensize(0)
	                alex.goto(x + s, y + t)
	    alex.goto(s,t)
	turtle.update()
	wn.exitonclick()

It looks like this:
![straightRayBurst](straightRayBurst.png)

This image below is just a repeat of the previous with some different parameters, mostly increasing the randomness:

![wobblyRayBurst](wobblyRayBurst.png)

I wanted to try something a little more challenging, so I made a couple of functions to get more control over the image. 
The RGB color generator is still limited; later I make one with better control.

	import random
	import turtle
	# Draws three concentric sets of crooked rays, emerging from darkness
	def colorGen(sat = 1, val = 1):
	    """Generates random RGB values. sat range 0-1, val range = 0-1"""
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
	def timeTunnel(repeats = 1,zigzag = 10, stepVar = 1):
	    for i in range(repeats):
	        alex.goto(0,0)
	        alex.seth(random.uniform(0,360)) # set heading
	        h1 = alex.heading() # get heading
	        alex.color(colorGen(val=0))
	        for j in range(10):
	            alex.down()
	            alex.forward(abs(round(random.gauss(10, stepVar),0))) # abs limits motion to forward
	            alex.seth(h1 + random.gauss(0,zigzag))
	            x = alex.xcor()
	            y = alex.ycor()
	            alex.color(colorGen(val = j/10))
	            h2 = alex.heading()
	        for k in range(3):
	            alex.down()
	            alex.seth(h2 + random.gauss(0, zigzag))
	            h3 = alex.heading()
	            for k2 in range(10):
	                alex.color(colorGen(val = k2/10))
	                alex.seth(h3 + random.gauss(0,zigzag))
	                alex.forward(abs(round(random.gauss(10, stepVar), 0)))
	            alex.up()
	            m = alex.xcor()
	            n = alex.ycor()
	            h4 = alex.heading()
	            for l in range(2):
	                alex.color(colorGen())
	                alex.down()
	                alex.seth(abs(h4 + random.gauss(0,zigzag)))
	                h5 = alex.heading()
	                for l2 in range(10):
	                    alex.color(colorGen(val = l2/10))
	                    alex.seth(h5 + random.gauss(0,zigzag))
	                    alex.forward(abs(round(random.gauss(10,stepVar),0)))
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
	timeTunnel(300)
	turtle.update()
	wn.exitonclick()

![concentricRays1](concentricRays1.png)

By setting the variation parameters to 0, you get a straighter version:
![concentricRays1_NoVar](concentricRays1_NoVar.png)

Here I added a little spiral and set the length of each increment to a couple of pixels. Using all these nested loops is probably a very inefficient way to do this, but it works, and it looks pretty cool:
![concentricRays2](concentricRays2.png)

This bit of code adds a better color generator - this time with control over hue, saturation and value:

	import random
	import turtle
	import math
	# Draws three sets of concentric rays with a sort of spiral galaxy effect.
	# Small step size and multiple nested loops runs quite slowly. Probably not the most efficient code.
	def hueGen(hue = 0,val = 1, sat=1):
	    """Generates a 360 degree range of hues
	    sat of 1 is full saturation, 0 is B & W.
	    val of 1 is full color, 0 is black"""
	    if 0 <= hue < 60:
	        r = 1
	        g = (hue/59) + (1-sat)*(59-hue)/59
	        b = 1 - sat
	        hueOut = (r*val,g*val,b*val)
	    elif 60 <= hue < 120:
	        r = ((1-(hue-60)/59) + (1-sat)*(1-(119-hue)/59))
	        g = 1
	        b = 1 - sat
	        hueOut = (r*val,g*val,b*val)
	    elif 120 <= hue < 180:
	        r = 1 - sat
	        g = 1
	        b = ((hue-120)/59) + (1-sat)*(179-hue)/59
	        hueOut = (r*val,g*val,b*val)
	    elif 180 <= hue < 240:
	        r = 1 - sat
	        g = (1-(hue-180)/59) + (1-sat)*(1-(239-hue)/59)
	        b = 1
	        hueOut = (r*val,g*val,b*val)
	    elif 240 <= hue < 300:
	        r = ((hue-240)/59) + (1-sat)*(299-hue)/59
	        g = 1 - sat
	        b = 1
	        hueOut = (r*val,g*val,b*val)
	    elif 300 <= hue < 360:
	        r = 1
	        g = 1 - sat
	        b = (1-(hue-300)/59) + (1-sat)*(1-(359-hue)/59)
	        hueOut = (r*val,g*val,b*val)
	    elif hue >= 360:
	        hueOut = hueGen(hue % 360, val, sat)
	    return hueOut
	def timeTunnel(repeats = 1,zigzag = 10, stepVar = 1, curve = 0):
	    "Draws fuzzy concentric circles. zigzag is sd of randomgauss, stepVar is sd of length, curve is a multiplier that gives a spiral effect"
	    foo = 0
	    for i in range(repeats):
	        alex.goto(0,0)
	        alex.seth(random.uniform(0,360)) # set heading
	        h1 = alex.heading() # get heading
	        alex.color(hueGen(hue = i))
	        for j in range(50):
	            alex.down()
	            alex.forward(abs(round(random.gauss(2, stepVar),0))) # abs limits motion to forward
	            alex.seth(h1 + curve*j + random.gauss(0,4*zigzag))
	            x = alex.xcor()
	            y = alex.ycor()
	            alex.color(hueGen(hue = i*j, val = j/50)) # 1 - 51
	            h2 = alex.heading()
	        for k in range(2):
	            alex.down()
	            alex.seth(h2)
	            for k2 in range(50):
	                alex.color(hueGen(hue = i+j+k*k2, val = k2/50))
	                alex.seth(h2 + curve*k2 + random.gauss(0,2*zigzag))
	                alex.forward(abs(round(random.gauss(2, stepVar), 0)))
	            alex.up()
	            m = alex.xcor()
	            n = alex.ycor()
	            h3 = alex.heading()
	            # h4 = alex.heading()
	            for l in range(4):
	                alex.color(hueGen(hue = 9*l))
	                alex.down()
	                alex.seth(h3)
	                # h5 = alex.heading()
	                for l2 in range(50):
	                    alex.color(hueGen(hue = l*l2*2.449, val = l2/50))
	                    alex.seth(h3 + curve*l2 + random.gauss(0,zigzag))
	                    alex.forward(abs(round(random.gauss(2,stepVar),0)))
	                alex.up()
	                alex.goto(m, n)
	            alex.goto(x, y)
	        alex.up()
	turtle.tracer(0, 0)
	wn = turtle.Screen()
	wn.colormode(1)
	turtle.bgcolor("black")
	alex = turtle.Turtle()
	alex.speed(10)
	alex.pensize(0)
	alex.ht()
	timeTunnel(500,1, 1, .5)
	turtle.update()
	wn.exitonclick() 

![concentricRays3](concentricRays3.png)

By making the hue a function of direction using alex.heading(), you get a nice rainbow effect:
![rainbowGalaxy](rainbowGalaxy.png)

Lastly, this code makes a nice looking set of colored sine waves that curve around in an interesting way:
	def waves(repeats = 1):
	    """Draws nested colored sinusoids emerging from darkness"""
	    for i in range(repeats):
	        alex.up()
	        alex.color(hueGen(i, .5*i/repeats, .5))
	        alex.goto(-315,315 - i)
	        alex.seth(45) # set heading
	        x = alex.xcor()
	        y = alex.ycor()
	        f = i + 1
	        for j in range(630):
	            x = alex.xcor()
	            alex.goto(x + 1, y + 25*sin(8*j/f + i/25)) # plot sines
	            alex.down()
	            x = alex.xcor()

	turtle.tracer(0, 0)
	wn = turtle.Screen()
	wn.colormode(1)
	turtle.bgcolor("black")
	alex = turtle.Turtle()
	alex.speed(10)
	alex.pensize(2)
	alex.ht()
	waves(700)
	turtle.update()
	wn.exitonclick()
![sineWaves1](sineWaves1.png)

Setting both the value and saturation to .5 gives this:
![sineWaves2](sineWaves2.png)

setting the saturation to 0 gives a grayscale image:
![sineWaves3](sineWaves3.png)

