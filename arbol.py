import turtle
import random
colors = ['#F21818','#01BC1F','#1F12F7','#9212F7','#D9F712','#03C3F9','#B403F9']
t = turtle.Turtle()
w = t.getscreen()
t.hideturtle()
t.speed(0)
#w.bgcolor('black')
t.penup()
t.setposition(0,-300)
t.left(90)
t.pendown()

def arbol(f,p):
    t.pensize(3)
    if p == 0:
        t.dot(random.randint(9,12),random.choice(colors))
        return
    else:
        t.forward(f)
        t.left(30)
        arbol(f*random.uniform(0.7,0.9),p-1)
        t.right(60)
        arbol(f*random.uniform(0.7,0.9),p-1)
        t.left(30)
        t.back(f)
        
arbol(140,9)

turtle.done()