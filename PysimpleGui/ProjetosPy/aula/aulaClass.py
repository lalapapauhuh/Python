#class
#syntaxe

#Marca, RAM, Placa de video
from time import sleep
class Computador:
    def __init__(self, marca, ram, placa_de_video):
        self.marca = marca
        self.ram = ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Ligando....')
        sleep(2)
        print('Seja Bem-Vindo!')

    def Desligar(self):
        print('Desligando...')
        sleep(2)
        print('Computador Desligado!')

    def ExibirInfos(self):
        print(self.marca, self.ram, self.placa_de_video)

computador1 = Computador('Lenovo', '4gb', 'Nvidia')
computador1.Ligar()
computador1.ExibirInfos()
computador1.Desligar()
# Ligar, Desligar, Exibir, Configurações