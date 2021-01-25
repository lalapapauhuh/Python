#par ou impar game
from random import randint
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'
}
print('{} Par ou Ímpar Game {}'.format('='*10, '='*10))

while True:
    n_vc = int(input('Digite um valor: '))
    opcao = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    n_pc = randint(0,10)
    total = n_pc + n_vc

    if opcao == 'P':
        if total % 2 == 0:
            print(f'Você: {n_vc} e o computador: {n_pc}. Total {total} é PAR')
            print('{}GANHOU!!!{}'.format(cores['verde'], cores['limpa']))
            print('Pode jogar de novo')
            print('='*50)
        else:
            print(f'Você: {n_vc} e o computador: {n_pc}. Total {total} é IMPAR')
            print('{}PERDEU :( {}'.format(cores['vermelho'], cores['limpa']))
            break
    elif opcao == 'I':
         if total % 2 == 1:
             print(f'Você: {n_vc} e o computador: {n_pc}. Total {total} é IMPAR')
             print('{}GANHOU!!!{}'.format(cores['verde'], cores['limpa']))
             print('Pode jogar de novo')
             print('='*50)
         else:
             print(f'Você:{ n_vc} e o computador: {n_pc}. Total {total} é PAR')
             print('{}PERDEU :< {}'.format(cores['vermelho'], cores['limpa']))
             break
    else:
        print('Jogada invalida. Tente novamente')
print('Fim')
