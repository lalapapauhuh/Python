# Criação da classe
class Cachorro:
    
    especie = 'Canis familiaris'  # Atributo de classe(para toda classe)
    def __init__(self, nome, idade): # metodo dunder
        self.nome = nome
        self.idade = idade
        
    def __str__(self):  # metodo dunder
        return f'{self.nome} tem {self.idade} anos.'

    def latir(self, som):
        return f'{self.nome} late {som}'


class JackRussellTerrier(Cachorro):
    def latir(self, som='uauuauauau'):
        return super().latir(som)


class Dachshund(Cachorro):
    def latir(self, som='rrrhh auauau'):
        return f'{self.nome} está latindo {som}'


class Bulldog(Cachorro):
    def latir(self, som='uOuoUououou'):
        return f'{self.nome} está latindo {som}'

class GoldenRetriever(Cachorro):
    def latir(self, som='AUAUAUAU'):
        return super().latir(som)


miles = JackRussellTerrier('Miles', 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
marley = GoldenRetriever('Marley', 6)


print(miles.latir('grrr'))
print(jim.latir())
print(marley.latir())
