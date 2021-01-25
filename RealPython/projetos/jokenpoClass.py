import random
from time import sleep

# Pega a escolha do usuario
def get_usuario():
    while True:
        print('Pedra, Papel, Tesoura')
        escolha = input('Escolha: ').strip().lower()[:2]
        if escolha in 'ped':
            escolha = 'Pedra'
            break
        elif escolha in 'pap':
            escolha = 'Papel'
            break
        elif escolha in 'tes':
            escolha = 'Tesoura'
            break
        else:
            print('Escolha invalida. Tente novamente')

    return escolha

# Pega escolha do computador
def get_computador():
    op = ['Pedra', 'Papel', 'Tesoura']
    escolha = random.choice(op)
    return escolha

# Faz a lógica do jogo
def determine_vencedor(eu, pc):
    if eu == pc:
            return '\033[33mEmpate\033[m'

    elif eu == 'Pedra':
        if pc == 'Papel':
            return '\033[31mComputador ganhou\033[m'
        else:
            return '\033[32mVocê ganhou\033[m'

    elif eu == 'Papel':
        if pc == 'Tesoura':
            return '\033[31mComputador ganhou\033[m'
        else: 
                return '\033[32mVocê ganhou\033[m'

    elif eu == 'Tesoura':
        if pc == 'Pedra':
            return '\033[31mComputador ganhou\033[m'
        else:
            return '\033[32mVocê ganhou\033[m'

# Programa  
while True:
    print('-='*25)
    usuario = get_usuario()  # chama o funcao get_user
    computador = get_computador() #chama funcao get comput
    print('JO')
    sleep(0.3)
    print('KEN')
    sleep(0.3)
    print('PÔ')
    sleep(0.3)
    print(f'VOCÊ: {usuario}\t COMPUTADOR: {computador}')
    print(f'\t{determine_vencedor(usuario, computador)}')


# Apos 2s pergunta se quer jogar de novo
    sleep(2)
    revanche = input("Jogar de Novo? (s/n): ").lower()[0]
    if revanche != 's':
        break

