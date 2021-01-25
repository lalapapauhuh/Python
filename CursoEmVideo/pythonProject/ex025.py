import itertools

nome = str(input('Digite seu nome completo: '))
nome = nome.lower()

s = nome.find('silva')
if s < 0:
    print('Você não tem Silva no seu nome!')
elif s >=0 :
    print('Você tem Silva no seu nome!')
