# .extend() para adicionar varios items como append
import math

'''def raiz_quadrada(listanum):
    raiz = []
    for num in listanum:
        raiz.append(math.sqrt(num))
    return raiz
'''


'''# Usando compreensão de lista
def raiz_quadrada(numeros):
    return [math.sqrt(num) for num in numeros]
'''

'''def raiz_quadrada(numeros):
    raiz = []
    n = len(numeros)
    for i, num in enumerate(numeros): # i é o indice,  num os valores
        print(f'Processando o numero: {num}')
        raiz.append(math.sqrt(num))
        print(f'Completando: {int(i+1) / n*100}%')
    return raiz'''


numeros = [16, 25, 81, 144, 169]
resp = raiz_quadrada(numeros)
print(resp)