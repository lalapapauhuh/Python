# Validando entrada de dados
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, KeyboardInterrupt, TypeError):
            print('\033[31mValor não é valido\033[m')
            continue 
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, KeyboardInterrupt, TypeError):
            print('\033[31mValor não é valido\033[m')
            continue 
        else:
            return n

# Programa principal
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')
flat_num = leiafloat('Digite um float: ')
print(f'Você digitou o {flat_num}')
