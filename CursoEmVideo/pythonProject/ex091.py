# Jogo de dados
from time import sleep
from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
}
rank = []
print('Valores sorteados: ')
for key, valor in jogo.items():
    print(f'{key} tirou {valor} no dado.')
    sleep(2)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('    RANK DOS VENCEDORES  ')
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)