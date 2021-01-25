class Clientes:
    def __init__(self, nome, email, idade, endereco):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.endereco = endereco

    def cadastrar_cliente(self):
        self.nome = str(input('Digite seu nome: '))
        self.email = str(input('Digite seu email: '))
        self.idade = str(input('Digite seu idade: '))
        self.endereco = str(input('Digite seu endereço: '))
    
    def logar_cliente(self):
        print('Digite seu email:')
        self.email = str(input())
        print('Digite sua senha: ')
        senha = str(input())
        abrir_loja()
        