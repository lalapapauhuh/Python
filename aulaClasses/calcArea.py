
class Ponto:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia_origem(self):
        return ((self.x**2)+(self.y**2)**0.5)

    def __str__(self):
        return 'x = '+ str(self.x) + ', y = '+str(self.y)


class Retangulo:
    def __init__(self, local, base, altura):
        self.local = local
        self.base = base
        self.alt = altura
         
    
    def __str__(self):
        return 'altura ' + str(self.alt) + ', base ' + str(self.base)

    def area(self):
        return self.alt * self.base

    def perimetro(self):
        return (self.alt*2) + (self.base*2)
    
    def transpose(self):
        aux = self.base
        self.base = self.alt
        self.alt = aux
        
    def dentro(self, x, y):
        if x >= 0 and y >= 0:
            if x < self.base and y < self.alt:
                return True
            else:
                return False
        else:
            return False

r = Retangulo(Ponto(0,0), 10, 5)

area = r.area()
perimetro = r.perimetro()
print(r)
print(f'A area do retangulo {r} é {area}')
print(f'O perimetro do retangulo {r} é {perimetro}')
r.transpose()
print(r)
# teste

r1 = Retangulo(Ponto(8,0), 10, 5)
print(r1.dentro(8, 0))
