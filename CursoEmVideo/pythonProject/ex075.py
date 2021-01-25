#analise de dados em uma tupla
num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quatro número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 aparece na posição {num.index(3)}.')
else:
    print('O valor 3 não foi digitado.')
    print(f'Números pares: ', end=' ')
for n in num:
    if n%2 == 0:
        print(n, end=' ')
