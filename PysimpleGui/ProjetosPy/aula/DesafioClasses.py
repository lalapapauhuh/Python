# DESAFIO CLASSES E METODOS
'''Crie uma classe carro que tenha no mínimo 3 propriedades,
 para a classe carro e no mínomo 3 metodos para ela'''

from time import sleep
cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'pretob': '\033[7;30m'
         }
class Carro:

    def __init__(self, marca, ano, cor, combustivel):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel
    
    def Ligar(self):
        print('{}Ligando carro...{}'.format(cores['pretob'], cores['limpar']))
        sleep(2)
        print('Carro ligado!!')
        sleep(3)

    def Andar(self):
        print('O freio de mão foi puxado')
        print('O carro começa a andar')
        sleep(3)

    def Acelerar(self):
        print('{}O acelerador é acionado{}'.format(cores['verde'], cores['limpar']))
        print('{}O carro começa a acelerar{}'.format(cores['verde'], cores['limpar']))
        sleep(3)

    def Frear(self):
        print('{}os freios são acionados{}'.format(cores['vermelho'], cores['limpar']))
        print('{}O carro começa a frear{}'.format(cores['vermelho'], cores['limpar']))
        sleep(3)

    def Desligar(self):
        print('{}Desligando o motor{}'.format(cores['pretob'], cores['limpar']))
        sleep(2)
        print('Carro Desligado!')

carro1 = Carro('Ford', '2015', 'preto', 'flex')
carro1.Ligar()
carro1.Andar()
carro1.Acelerar()
carro1.Frear()
carro1.Desligar()