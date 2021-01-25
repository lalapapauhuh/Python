import random
import turtle

def na_tela(w,t):
    lado_esquerda = - w.window_width()/2
    lado_direito = w.window_width()/2
    lado_cima = w.window_height()/2
    lado_baixo = -w.window_height()/2

    posicaoX = t.xcor()
    posicaoY = t.ycor()

    stillIn = True
    if posicaoX > lado_direito or posicaoX < lado_esquerda:
        t.up()
        t.goto(0,0)
        t.down()
        stillIn = False
        
    if posicaoY > lado_cima or posicaoY < lado_baixo:
        t.up()
        t.goto(0,0)
        t.down()
        stillIn = False
    
    return stillIn


wn = turtle.Screen()
wn.bgcolor('#182858')
tarta = turtle.Turtle()
tarta.color('#DAF7A6')
tarta.shape('turtle')


cont = 3
while True:
    
    vida = na_tela(wn,tarta)
    if vida == False:
        cont -= 1
    if cont == 0:
        break

    coin = random.randrange(0,2)
    if coin == 0:
        tarta.left(90)
    else:
        tarta.right(90)

    tarta.forward(100)

tarta.goto(20, -15)
tarta.write('GAME OVER')


wn.exitonclick()
