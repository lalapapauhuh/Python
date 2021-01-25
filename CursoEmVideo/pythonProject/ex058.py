#adivinhe o numero 2.0
import random
from time import sleep
cores = { 'limpa': '\033[m',
          'vermelho': '\033[31m',
          'verde': '\033[32m',
          'ciano': '\033[46m'
}
n = random.randint(0,20)
print('='*10,'Adivinhe o número entre 0 e 20 !!!', '='*10)
num = 0
contador = 0
acertou = False

while not acertou:
    num = int(input('Digite um número entre 0 e 20: '))
    print('PROCESSANDO...')
    sleep(2)
    if num == n:
        print('{}Parabéns você acertou, o número escolhido era mesmo o {}!!{}'.format(cores['verde'], n, cores['limpa']))
        acertou = True
    else:
        if num > n:
            print('{}Que pena você errou. Tente um número MENOR ...{}'.format(cores['vermelho'], cores['limpa']))
        elif num < n:
            print('{}Que pena você errou. Tente um número MAIOR ...{}'.format(cores['vermelho'], cores['limpa']))
    contador += 1

print('Você precisou de {} tentativas para acertar'.format(contador))