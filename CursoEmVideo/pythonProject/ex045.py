#joquenpô
from random import randint
from time import sleep
cores = {'limpa':'\033[m',
         'azul':'\033[7;36;40m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
}
print('{}{:.^20}{}'.format(cores['azul'], ' JOKENPÔ!!! ', cores['limpa']))

print(' 1 - PEDRA\n 2 - PAPEL\n 3 - TESOURA')
jogo = (' ','Pedra', 'Papel', 'Tesoura')
vc = int(input('Digite o número da opção acima: '))
bot = randint(1,3) #sorteia um numero entre 1 e 3, será necessario pois são as posições dos itens em 'jogo'

if vc == 1 or vc == 2 or vc == 3: # não funcionará caso o numero nao seja 1 2 ou 3
 sleep(0.5)
 print('\nJOOO', end=' ')
 sleep(0.5)
 print('KENN', end=' ')
 sleep(0.5)
 print('POOO')
 print(' Você: {}\n Bot: {}'.format(jogo[vc], jogo[bot]))
 sleep(1)
 print('='*20)
else:
 print('Jogada invalida')


if vc == bot:
    print(' Empate! ')
elif vc == 1: #se vc escolher pedra
    if bot == 2:
        print('{}Você perdeu :({}'.format(cores['vermelho'], cores['limpa']))
    elif bot == 3:
        print('{}Você venceu :){}'.format(cores['verde'], cores['limpa']))
elif vc == 2: # se vc escolher papel
    if bot == 1:
        print('{}Você venceu :){}'.format(cores['verde'], cores['limpa']))
    elif bot == 3:
        print('{}Você perdeu :({}'.format(cores['vermelho'], cores['limpa']))
elif vc == 3: # se vc escolher tesoura
    if bot == 1:
        print('{}Você perdeu :({}'.format(cores['vermelho'], cores['limpa']))
    elif bot == 2:
        print('{}Você venceu :){}'.format(cores['verde'], cores['limpa']))
