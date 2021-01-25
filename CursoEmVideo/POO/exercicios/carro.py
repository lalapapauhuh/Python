class Carro:
    def __init__(self, cor, kmrodados):
        self.cor = cor
        self.rodados = kmrodados

    def __str__(self):
        return f'O carro {self.cor}, rodou {self.rodados} km.'


carrinho1 = Carro('Azul', 20000)
carrinho2 = Carro('Vermelho', 30000)

print(carrinho1)
print(carrinho2)