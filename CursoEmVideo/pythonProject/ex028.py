#adivinhe o numero
import random
from time import sleep 
# Classe
n = random.randint(0,5) # funcao gerar o numero
print('Adivinhe o número!!!')
num = int(input('Digite um número entre 0 e 5: ')) # funcao perguntar o numero
if n == num: # funcao verificar se esta certo
    print('PROCESSANDO...')
    sleep(2)
    print('Parabéns você acertou, o número escolhido era mesmo o {}!!'.format(n))
else:
    print('PROCESSANDO...')
    sleep(2)
    print('Que pena você errou. Não era o {} e sim {} :('.format(num,  n))