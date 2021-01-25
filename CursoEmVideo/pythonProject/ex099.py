# função que descobre o maior
from time import sleep
def maior(* numeros):
    print('=' * 30)
    print('Analisando os valores passados...')
    sleep(0.5)
    for n in numeros:
        print(f'{n}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo')
    sleep(0.4)
    if len(numeros) != 0:
        print(f'O maior valor informado foi {max(numeros)}.')


#   Programa Principal
maior(1, 2, 3, 4)
maior(4, 2, 5, 9, 0)
maior(0, 8, 3)
maior(7, 6)
maior()