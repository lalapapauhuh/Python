import vendedor
import cliente
from cliente import cadastrar_cliente
from cliente import logar_cliente
from vendedor import novo_produto

def linha():
    print('-'*50)

def titulo(msg):
    linha()
    print(f'\033[34m{msg}\033[m'.center(50))
    linha()

def menu():
    print('\033[32m1 - Login\n2 - Cadastrar\033[m')
    linha()
    op = input('Digite sua opção: ')
    if op == 0 : 
        novo_produto()
    elif op == 1:
        cadastrar_cliente()
    elif op == 2:
        logar_cliente()

    
    
