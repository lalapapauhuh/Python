from random import choice
from time import sleep

 # Logica do jogo 
def jogo(e, p):
    if e == p:
        return '\033[33mEmpate\033[m'

    elif e == 'Pedra':
        if p == 'Papel':
            return '\033[31mComputador ganhou\033[m'
        else:
            return '\033[32mVocê ganhou\033[m'

    elif e == 'Papel':
        if p == 'Tesoura':
            return '\033[31mComputador ganhou\033[m'
        else: 
            return '\033[32mVocê ganhou\033[m'

    elif e == 'Tesoura':
        if p == 'Pedra':
            return '\033[31mComputador ganhou\033[m'
        else:
            return '\033[32mVocê ganhou\033[m'

while True:
    # Computador Escolhe
    op = ["Pedra", "Papel", "Tesoura"]
    pc = choice(op)
    print('-='*30)
    # Escolhendo e validando a escolha
    while True:
        print('Pedra, Papel ou Tesoura')
        eu = str(input('Escolha: ')).strip().lower()[:2]
        if eu in 'ped':
            eu = 'Pedra'
            break
        elif eu in 'pap':
            eu = 'Papel'
            break
        elif eu in 'tes':
            eu = 'Tesoura'
            break 
        else:
            print('Opção invalida tente novamente')

    print('JO')
    sleep(0.4)
    print('KEN')
    sleep(0.4)
    print('PÔ')

    print(f'\nVocê {eu}\t Computador {pc}:')
    print(f'\t{jogo(eu, pc)}')

    sleep(2)
    revanche = input('Jogar de novo? [S/N]:').upper()[0]
    if revanche != 'S':
        break