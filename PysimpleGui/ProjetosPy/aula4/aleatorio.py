import random
from time import sleep

print(random.random()) # Valor entre 0.0  1.0
print(random.uniform(4,10)) # Valor DECIMAL entre o 4 e 10
print(random.randint(10,100)) # Valor INTEIRO entre 10 e 100

cores = ['verde', 'vermelho', 'azul', 'amarelo', 'laranja']
print(random.choice(cores)) # Escolher uma opção dentro da lista

cartas_baralho = ['as', 'rei', 'dama', 'valete', 'dois', 'tres', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez']
random.shuffle(cartas_baralho) # Embaralha as cartas
print(cartas_baralho)

# DESAFIOS:
jogador = str(input('Escolha Cara ou Coroa? ')).upper().strip()
moeda = ['CARA', 'COROA']
resultado = random.choice(moeda)
print('Jogando a moeda...')
sleep(2)
print(f'Deu {resultado}')
if resultado == jogador:
    print('Parabéns você ganhou')
else:
    print('Que pena você perdeu')


