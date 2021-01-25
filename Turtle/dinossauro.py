import turtle

wn = turtle.Screen()
tarta = turtle.Turtle()
tarta.pensize(3)

arquivo = open(r"C:\Users\CASSIO\Documents\Python\Turtle\desenho.txt")

for linha in arquivo:
    item = linha.split()

    if item[0] == 'UP':
        tarta.up()

    elif item[0] == 'DOWN':
        tarta.down()

    else:
        tarta.goto(int(item[0]), int(item[1]))

arquivo.close()
wn.exitonclick()