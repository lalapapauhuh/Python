import turtle
from random import randint

def arvore(t, tam, s):
    if tam > 5:
        t.pensize(s)
        t.forward(tam)
        t.right(20) 
        arvore(t, tam-15, s-1)
        t.left(40)
        arvore(t, tam-15, s-1)
        t.right(20)
        t.backward(tam)
       

wn = turtle.Screen()
tarta = turtle.Turtle()
tarta.color('Green')
tarta.speed(9)
sz = 5
tarta.pensize(sz)
tarta.left(90)
tarta.up()
tarta.backward(100)
tarta.down()

arvore(tarta, 75, sz)

wn.exitonclick()