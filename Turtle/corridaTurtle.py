import turtle
import random
from time import sleep

def linha(t):
    t.up()
    t.goto(300,-200)
    t.down()
    t.left(90)
    t.pensize(3)
    t.forward(500)
    t.up()
    t.home()
    t.color('CornflowerBlue')
    t.shapesize(1.3)

def anda(t):
    t.forward(random.randint(10, 50))
        
wn = turtle.Screen()
wn.bgcolor('PaleGoldenRod')

# CRIANDO AS TARTARUGAS
blastoise = turtle.Turtle()
blastoise.shape('turtle')
blastoise.color('Black')
linha(blastoise)

torkoal = blastoise.clone()
torkoal.color('DarkRed')

torterra = blastoise.clone()
torterra.color('DarkGreen')

# LISTA DOS COMPETIDORES
competidores = [blastoise, torkoal, torterra]

# CONTADOR DE VITORIAS
vitBlas = 0
vitTork = 0
viTerra = 0

for i in range(3): # REPETE TUDO 3X
    blastoise.goto(-250, 150) # INDO PRA LARGARDA
    torkoal.goto(-250, 30) # INDO P LARGADA
    torterra.goto(-250, -100) # INDO P LARGADA
    sleep(0.5)

    for i in range(60):
        # SORTEIA UM DOS COMPETIDORES PRA ANDAR
        anda(random.choice(competidores))

        if blastoise.xcor() > 300: # SE ESSE GANHAR
            print('Blastoise ganhou')
            vitBlas += 1 # SOMA +1 VITORIA
            break
        elif torkoal.xcor() > 300: # SE ESSE GANHAR
            print('Torkoal ganhou')
            vitTork += 1  # SOMA +1 VITORIA
            break
        elif torterra.xcor() > 300: # SE ESSE GANHAR
            print('Torterra ganhou')
            viTerra += 1 # SOMA +1 VITORIA
            break
    sleep(1)

# PLACAR FINAL
print(f'\nBlastoise {vitBlas}\nTorkoal {vitTork}\nTorterra {viTerra}')

wn.exitonclick()