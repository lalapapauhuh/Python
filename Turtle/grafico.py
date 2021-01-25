import turtle

def desenhaBarra(t, altura):
    """Faca a tartaruga t desenhar uma barra, de altura `altura`."""
    t.begin_fill()               # comece preenchendo o perfil
    t.left(90)               # Apontar
    t.forward(altura)        # Desenha o lado esquerdo
    t.right(90)
    t.write('  ' + str(altura))
    t.forward(40)            # largura da barra no topo
    t.right(90)
    t.forward(altura)        # e abaixo novamente!
    t.left(90)               # coloca a tartaruga na posição que a encontramos
    t.end_fill()                 # pare de preencher o perfil

wn = turtle.Screen()             # Inicializa a janela
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # cria tess
tess.up()
tess.goto(0,0)
tess.down()
tess.forward(200)
tess.forward(-400)
tess.up()
tess.color('Blue')
tess.goto(-150,0)
tess.down()


xs = [48, 117, 154, 40, 60, 98, 114]
for v in xs:                 # assuma que xs e tess estão prontas
    desenhaBarra(tess, v)
tess.home()
wn.exitonclick()
