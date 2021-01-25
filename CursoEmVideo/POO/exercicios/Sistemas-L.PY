import turtle

def criando_sistema(vzs, letra):
    inicio = letra
    fim = ""
    for i in range(vzs):
        fim = gerando_sistema(inicio)
        inicio = fim
    
    return fim


def gerando_sistema(msg):
    novo = ''
    for caracter in msg:
        novo = novo + regra_sistema(caracter)

    return novo


def regra_sistema(c):
    novo = ''
    if c == 'F':
        novo = 'F-F++F-F' 
    else:
        novo = c
        
    return novo


def desenhando(t, cod, angulo, distancia):
    for item in cod:
        if item == 'F':
            t.forward(distancia)
        elif item == 'B':
            t.backward(distancia)
        elif item == '+':
            t.right(angulo)
        elif item == '-':
            t.left(angulo)
        else:
            print('Erro:', item, 'codigo desconhecido')


def main():
    sistema = criando_sistema(4, 'F')
    wn = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.speed(0)

    tarta.up()
    tarta.goto(0,-200)
    tarta.down()
    desenhando(tarta, sistema, 60, 5)


    wn.exitonclick()

main()