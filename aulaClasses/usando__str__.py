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

    def caminho_medio(self, valor):
        media_x = (self.x + valor.x)/2
        media_y = (self.y + valor.y)/2
        return Ponto(media_x, media_y)

a = Ponto(3, 4)
b = Ponto(5, 12)
media = a.caminho_medio(b)

print(media)
print(media.getX())
print(media.getY())