import turtle
import random

# creating turtle object
t = turtle.Turtle()
t.speed(5)
# to activate turtle graphics Screen
w = turtle.Screen()
w.bgcolor("black")
#moon
# for making our moon looking up the pen
t.up()

# going at the specific coordinated
t.goto(300, 170)

# took down the pen to start drawing
t.down()

# giving color to turtle's pen
t.color("#f2e7a7")

t.begin_fill() # start filling the color
t.circle(50) # making our moon
t.end_fill() # stop filling the color
t.hideturtle()

#Earth
# for making our moon looking up the pen
t.up()

# going at the specific coordinated
t.goto(-200, -200)

# took down the pen to start drawing
t.down()

# giving color to turtle's pen
t.color("#287AB8")

# start filling the color
t.begin_fill()

# making our moon
t.circle(150)

# stop filling the color
t.end_fill()


#Africa continent
t.up()
t.goto(-200, -50)
t.down()
t.color("green")
t.fillcolor('green')
t.begin_fill()


t.forward(10)
t.right(45)
t.forward(10)
t.left(45)
t.forward(20)
t.right(45)
t.forward(10)
t.left(20)
t.forward(5)
t.right(30)
t.forward(10)
t.left(30)
t.forward(30)
t.right(50)
t.forward(10)
t.right(60)
t.forward(40)
t.right(20)
t.forward(10)
t.left(50)
t.forward(10)
t.right(20)
t.forward(30)
t.left(50)
t.forward(10)
t.right(50)
t.forward(10)
t.right(50)
t.forward(5)
t.right(45)
t.forward(25)

t.right(45)
t.forward(5)
t.left(45)
t.forward(5)

t.right(45)
t.forward(5)
t.right(45)
t.forward(5)

t.left(40)
t.forward(10)
t.left(40)
t.forward(10)
t.right(40)
t.forward(10)
t.right(40)
t.forward(10)

t.left(140)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)

t.right(30)
t.forward(20)

t.right(20)
t.forward(10)
t.right(20)
t.forward(10)
t.right(30)
t.forward(10)
t.left(45)
t.forward(10)
t.right(45)
t.forward(20)
t.right(45)
t.forward(10)

# stop filling the color
t.end_fill()


#America continent
t.up()
t.goto(-340,0)  # America starting point
t.down()
t.color("green")
t.fillcolor('green')
t.begin_fill()

t.right(45)
t.forward(10)

t.right(45)
t.forward(10)
t.left(45)
t.forward(10)

t.right(45)
t.forward(10)
t.left(45)
t.forward(10)

t.left(45)
t.forward(10)
t.left(45)
t.forward(10)

t.right(45)
t.forward(10)
t.left(45)
t.forward(10)

t.right(45)
t.forward(10)
t.right(15)
t.forward(10)
t.right(30)
t.forward(10)

t.left(30)
t.forward(10)

t.left(30)
t.forward(10)

t.right(30)
t.forward(10)

t.left(10)
t.forward(10)

t.right(30)
t.forward(5)

t.left(10)
t.forward(1)

t.left(90)
t.forward(10)
t.right(45)
t.forward(10)

t.left(90)
t.forward(10)
t.right(45)
t.forward(10)

t.left(90)
t.forward(10)
t.right(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)

t.left(90)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)

t.left(90)
t.forward(10)
t.right(45)
t.forward(10)


t.left(90)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)
t.right(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)


t.left(90)
t.forward(15)
t.left(45)
t.forward(15)

t.right(90)
t.forward(10)
t.left(45)
t.forward(10)
t.left(30)
t.forward(5)

t.left(35)
t.forward(20)

t.forward(10)

t.left(20)
t.forward(50)
t.left(20)
t.forward(60)

t.left(20)
t.forward(50)

t.end_fill()

#small circle
t.up()
t.goto((-328,50))
t.down()
t.color("white")
t.circle(170)

#middle circle
t.up()
t.goto((-330,75))
t.down()
t.circle(190)

# Big circle
t.up()
t.goto((-330,100))
t.down()
t.circle(220)

# large circle
t.up()
t.goto((-340,120))
t.down()
t.circle(240)

t.up()
t.goto(76,-115)
t.down()
t.right(188)
t.forward(400)
t.circle(90)
t.circle(80)
t.circle(70,180)

#satellite
t.color("#B2BEB5")

t.begin_fill() # start filling the color
t.circle(5) # making our moon
t.end_fill() # stop filling the color

t.hideturtle()
w.exitonclick()
