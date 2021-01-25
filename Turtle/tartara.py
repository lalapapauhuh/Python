import turtle
from time import sleep

wn = turtle.Screen()
wn.bgcolor("#575564")         # define a cor de fundo da janela

tess = turtle.Turtle()
tess.color("#74f6ff")               # tess fica azul
tess.pensize(3)                  # define a espessura da caneta

tess.forward(150)        # manda o tess se mover 150 unidades para frente
sleep(0.5)
tess.left(90)            # roda de 90 graus para a esquerda
sleep(0.5)
tess.forward(75)         # desenha o segundo lado do retângulo
tess.left(90) 
sleep(0.5)
tess.forward(150)
sleep(0.5)
tess.left(90)
tess.forward(75)

wn.exitonclick()
