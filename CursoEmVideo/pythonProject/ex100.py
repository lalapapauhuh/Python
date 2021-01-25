#Função para sortear e somar pares
from random import randint

def sorteia(lista):
    for cada in range(0, 5):
        lista.append(randint(0, 20))


def somaPar(lista):
    pares = 0
    for valor in (lista):
        if valor % 2 == 0:
            pares += valor
    print(f'Total da soma de pares: {pares}')


numeros = []
sorteia(numeros)
print(numeros)
somaPar(numeros)