'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, marca, material
Métodos: trocaCor e mostraCor'''

class Bola:
    def __init__(self, cor, marca, material):
        self.cor = cor
        self.marca = marca
        self.material = material
    
    def getCor(self):
        return self.cor
    
    def getMarca(self):
        return self.marca
    
    def getMaterial(self):
        return self.material
    
    def __str__(self):
        return 'Cor: '+ str(self.cor) + ', Marca: '+ str(self.marca) + ', Material: ' + str(self.material)

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        return self.cor

bola1 = Bola('Vermelha', 'Adidas', 'Couro')
bola2 = Bola('Verde', 'Brinquedo', 'Plastico')
bola3 = Bola('Branca', 'Penalty', 'Couro')

print(bola1)
bola1.trocaCor('Azul')
print(bola1)