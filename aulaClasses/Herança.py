class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanciaOrigem(self):
        return ((self.x **2) + (self.y **2)) **0.5
    
    def __str__(self):
        return 'X=' + str(self.x) + ' Y=' + str(self.y)


class HerdeiPonto(Ponto):
    def __init__(self, x, y, lugar):
        super().__init__(x,y)
        self.lugar = lugar
    
    def __str__(self):
        return 'X=' + str(self.x) + ' Y=' + str(self.y) + ' (' + str(self.lugar) +')' + '\n'



p = Ponto(5,10)
h = HerdeiPonto(7, 6, 'Aqui mesmo')

print(p)
print(h)