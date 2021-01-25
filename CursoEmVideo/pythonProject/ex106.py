# Interactive helping system in Python
from time import sleep
cor = {
    'limpar' : '\033[m',
    'azul': '\033[44m',
    'ciano' : '\033[46m',
    'vermelho': '\033[41m',
    'pretob' : '\033[7;40m'
}

def ajuda(nome):
    print(cor['pretob'])
    print(help(nome))
    print(cor['limpar'])


def titulo():
    print(f'{cor["ciano"]}{"-="*15}')
    print('  SISTEMA DE AJUDA PYTHON')
    print("-="*15)
    print(cor["limpar"])

#Programa principal
while True:
    titulo()
    funcao = str(input('Digite o nome da função: '))
    if funcao.upper() == 'FIM':
        print(f'{cor["vermelho"]}Programa Finalizado!{cor["limpar"]}')
        break
    else:
        sleep(1)
        ajuda(funcao)
