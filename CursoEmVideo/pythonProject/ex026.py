#quantas letras A
import itertools

frase = str(input('Digite uma frase: ')).lower().strip()
a = frase.count('a')
print('Na frase acima tem {} letras A'.format(a))
print('A letra "A" apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('E a letra "A" apareceu pela ultima vez na posição {}'.format(frase.rfind('a')+1))

