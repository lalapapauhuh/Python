import turtle

def risca(t, tam):
    for i in range(200):
        t.forward(tam)
        t.left(150)   #  MUDA AQUI PRA UM DESSES  90, 91, 120, 150, 160 ,180
        tam += 3    

wn = turtle.Screen()
wn.bgcolor('#581845')

lapis = turtle.Turtle()
lapis.color('#DAF7A6')
lapis.speed(0)
tamanho = 5
risca(lapis, tamanho)

wn.exitonclick()
