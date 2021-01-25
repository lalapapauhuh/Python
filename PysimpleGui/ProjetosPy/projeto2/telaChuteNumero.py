import PySimpleGUI as sg
from random import randint

class ChuteONumero:
    def __init__(self):
        self.resposta = 0
        self.valor_minimo = 1
        self.valor_maximo = 50
        self.tentar_novamente = True
        
    def Iniciar(self):
        self.gerar_numero()
        self.pedir_valor_random()
        try:
            while self.tentar_novamente == True:
                if int(self.meu_chute) > self.valor_random:
                    print('Muito alto. Tente um valor mais baixo!')
                    self.pedir_valor_random()
                elif int(self.meu_chute) < self.valor_random:
                    print('Muito baixo. Tente um valor mais alto!')
                    self.pedir_valor_random()
                elif int(self.meu_chute) == self.valor_random:
                    print(f'Parabéns você acertou. A resposta era {self.valor_random}')
                    self.tentar_novamente = False
        except:
            print('Favor digitar apenas números! ')
            self.Iniciar()
    
    def pedir_valor_random(self):
        self.meu_chute = input('Chute um Número entre 1 e 50: ')

    def gerar_numero(self):
        self.valor_random = randint(self.valor_minimo, self.valor_maximo)
chute = ChuteONumero()
chute.Iniciar()
