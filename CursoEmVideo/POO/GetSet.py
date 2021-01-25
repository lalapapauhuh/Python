class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual)/100

        # Getter - vai obter o valor
    @property
    def preco(self):
        return self._preco

        # Setter - vai configurar o valor na variavel
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


prod1 = Produto('Camiseta', 50)
prod1.desconto(10)
print(prod1.preco)

prod2 = Produto('Caneca', 'R$15')
prod2.desconto(10)
print(prod2.preco)