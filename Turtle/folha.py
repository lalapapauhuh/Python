import turtle

wn = turtle.Screen()
wn.bgcolor('LightGrey')

risco = turtle.Turtle()
risco.color('DimGrey')
risco.pensize(12)

for size in range(1,31,1):      
    risco.forward(size)          
    risco.right(26)              
risco.left(160)
risco.forward(50)
risco.up()
risco.goto(-60,-21)
risco.forward(5)
risco.down()
risco.right(65)        
risco.forward(-50)
risco.right(38)
risco.forward(70)

wn.exitonclick()