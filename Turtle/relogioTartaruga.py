import turtle

def carimbo():
    tarta.down()
    tarta.stamp()
    tarta.up()
    
def risca():
    tarta.down()
    tarta.forward(20)
    tarta.up()
    tarta.forward(20)

wn = turtle.Screen()
wn.bgcolor("DarkSlateGray")

tarta = turtle.Turtle()
tarta.color("FloralWhite")
tarta.shape("turtle")
angulo = 30

for anda in range(12):
    tarta.up()
    tarta.forward(120)
    risca()
    carimbo()
    tarta.backward(160)
    tarta.left(angulo)

wn.exitonclick()