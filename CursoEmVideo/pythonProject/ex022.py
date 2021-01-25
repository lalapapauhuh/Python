#usando as funções
import itertools
nome = str(input('Digite seu nome completo: '))
#maiusculo e minusculo
print('OLÁ',nome.upper())
print('olá', nome.lower())

#count sem espaços
n = (len(nome))
espaco = (nome.count(' '))
n = n - espaco
print('O nome tem {} letras'.format(n))
#print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

#quantas letras tem o primeiro nome
separa = (nome.split())
primeiro = separa[0]
print('O primeiro nome tem',len(primeiro), 'letras')
#print(('Seu nome tem {} letras').format(nome.find(' ')))

'''frase = str( 'Curso em Vídeo Python')
div = (frase.split())
print(div [2][2])'''

