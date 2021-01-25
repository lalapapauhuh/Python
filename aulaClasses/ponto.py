import math

# Criar a classe chamada Ponto
class Ponto:
    # Crio um novo ponto
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    # Metodo retorna o valor atual de X e Y
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def distancia_da_origem(self):
        return ((self.x **2)+(self.y **2)) **0.5

def distancia(ponto1, ponto2):
    x_dif = ponto2.getX() - ponto1.getX()  # 1
    y_dif = ponto2.getY() - ponto1.getY()  # 6
    
    dist = math.sqrt((x_dif**2) + (y_dif**2)) # √(6² + 1²) = √36 + 1  √37
    return dist # √37 = 6.082762..



a = Ponto(5, 3)
b = Ponto(6, 9)
# Os metodos são chamados com  variaval.nomeMetodo()
print(a.getX())
print(b.getY())
# Apenas chamando outro metodo
print(distancia(a,b))