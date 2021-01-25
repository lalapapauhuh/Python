#tuplas maior e menor
from random import randint
n = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(f'Valores sorteados: {n}')
print(f'O maior valor é: {max(n)}')
print(f'O menor valor é: {min(n)}')