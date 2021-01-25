#fatorial
numero = int(input('Digite um número: '))
fatorial = 1
print(f'Fatorial de {numero} é: ', end='')
while numero > 0:
    fatorial = fatorial*numero
    numero -= 1
print('{}'.format(fatorial))

