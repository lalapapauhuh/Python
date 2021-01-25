# Contador personalizado
from time import sleep

def contador(ini,fim,passo):
    linha()
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo += 1
    if ini > fim:
        decrementar(ini,fim,passo)
    while ini <= fim:
        print(f'{ini}', end=' ')
        ini += passo
        sleep(0.2)
    print('FIM')


def decrementar(ini,fim,passo):
    while ini >= fim:
        print(f'{ini}', end=' ')
        ini -= passo
        sleep(0.2)


def linha():
    print('-'*30)


contador(1,10,1)
contador(10,0,2)
linha()
inicio = int(input('Digite o inicio: '))
limite = int(input('Digite o limite: '))
passo = int(input('Digite a lógica para contar: '))
contador(inicio,limite,passo)