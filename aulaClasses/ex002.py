'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def getTam(self):
        return self.tamanho
    
    def __str__(self):
        return 'Tamanho: ' + str(self.tamanho)

    def mudarTamanho(self, novo):
        self.tamanho = novo
        return self.tamanho
    
    def area(self):
        return self.tamanho*4

    
n = Quadrado(50)
print(n)
n.mudarTamanho(100)
print(n)
print(n.area())