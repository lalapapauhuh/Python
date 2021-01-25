class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura
    def __str__(self):
        return 'Nome: '+ str(self.nome) + '\nIdade: '+ str(self.idade) + '\nPeso: '+ str(self.peso)+ '\nAltura: '+ str(self.altura) + '\n'

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura = self.altura + 0.05
        return self.idade, self.altura

    def engordar(self):
        self.peso += 2
        return self.peso
    
    def emagrecer(self):
        self.peso -= 2
        return self.peso
    
    def crescer(self):
        self.altura += 0.2
        return self.altura

p1 = Pessoa('cassio', 23, 72, 1.86)
p1.envelhecer()
print(p1)

p2 = Pessoa('João', 18, 65, 1.70)
p2.envelhecer()
p2.envelhecer()
p2.engordar()
print(p2)
p2.emagrecer()
p2.envelhecer()
p2.envelhecer()
p2.envelhecer()
print(p2)