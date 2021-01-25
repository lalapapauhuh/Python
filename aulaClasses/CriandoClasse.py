import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return 'x = ' + str(self.x ) + ', y = ' + str(self.y)

    def distancia(self, p2):
        xn = (p2.x - self.x)
        yn = (p2.y - self.y)
        dist = math.sqrt((xn**2)+ (yn**2))
        return dist

    def reflect_x(self):
      return Ponto(self.x, -self.y)

    def equacao_reta(self, p):
        yc = (p.y - self.y)
        xc = (p.x - self.x)
        if xc > 0:
            return (yc/xc)
        else:
            return 'Divisão por 0 ou negativo'
        


a = Ponto(4,11)
b = Ponto(6,15)
media = a.distancia(b)
print(f' a media é {media}')

espelho = a.reflect_x()
print(f' o espelho de {a} é {espelho}')

eq = a.equacao_reta(b)
print(f' A equacao da reta é {eq}')