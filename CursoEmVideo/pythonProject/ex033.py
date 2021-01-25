#qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2:
    maior = n1
else: maior = n2

if maior > n3:
    maior = maior
else: maior = n3

if n1 < n2:
    menor = n1
else: menor = n2

if menor < n3:
    menor = menor
else: menor = n3

print('O maior número digitado foi {} e o menor {}'.format(maior, menor))