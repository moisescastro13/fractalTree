import turtle 
tortuga = turtle.Turtle()
tortuga.speed(10)
tortuga.forward(-50)

for x in range(8):
    tortuga.forward(100)
    tortuga.circle(8)
    tortuga.left(45)
    tortuga.circle(-8)
tortuga.penup()
tortuga.forward(50)
tortuga.left(90)
tortuga.forward(125)
tortuga.pendown()
tortuga.circle(30)
tortuga.circle(-30)
tortuga.penup()
tortuga.left(180)
tortuga.forward(125)
tortuga.left(90)
tortuga.pendown()
tortuga.forward(15)
tortuga.right(90)
tortuga.forward(200)
tortuga.right(90)
tortuga.forward(30)
tortuga.right(90)
tortuga.forward(200)
turtle.done()