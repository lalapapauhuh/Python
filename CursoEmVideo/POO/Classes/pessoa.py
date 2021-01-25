from time import sleep
from random import randint
from datetime import datetime

class CriarPessoa:
    ano_atual = datetime.today().year
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}...')
        self.falando = True

    def parar_falar(self, tempo):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        sleep(tempo)
        print(f'{self.nome} terminou o assunto.')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer {alimento} agora pois está no meio do assunto')
            return

        print(f'{self.nome} está comendo {alimento}...')
        self.comendo= True

    def parar_comer(self, tempo):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        sleep(tempo)
        print(f'{self.nome} acabou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade  = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gerar_id():
        return randint(1000, 99999)

p1 = CriarPessoa.por_ano_nascimento('Cássio', 1997)
print(p1.idade)
p1.get_ano_nascimento()
print(p1.gerar_id())