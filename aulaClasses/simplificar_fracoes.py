def mdc(x1, x2):
    while x1%x2 != 0:
        nx1 = x1
        nx2 = x2

        # Trocando os valores de variavel
        x1 = nx2
        x2 = nx1 % nx2 # x2 recebe o resto da divisao entre nx1 e nx2
    return x2

class Fracao:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def simplifica(self):
        div_comum = mdc(self.num, self.den)
        self.num //= div_comum  # self.num =  self.num // div_comum
        self.den //= div_comum  # self.den = self.den // div_comum
    
    def __add__(self, n2):  # com __add__ podemos fazer soma de metodos criados
        novo_num = (self.num * n2.den) + (self.den * n2.num)
        novo_den = (self.den * n2.den)

        comum = mdc(novo_num, novo_den) # divisor comum entre eles
        n = novo_num // comum
        d = novo_den // comum

        return Fracao(n,d)


n1 = Fracao(1,8)
print(n1)
n1.simplifica()
print(n1)
n2 = Fracao(2,4)
n3 = n1 + n2
print(n3)
    
    