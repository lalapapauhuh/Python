# tratamento de valores
numero = 0
cont = 0
resultado = 0
saida = False

while not saida:
    if numero != 999:
        numero = int(input('Digite um número [999 para parar]: '))
        resultado += numero
        cont += 1
        saida = False
    else:
        cont -= 1
        resultado -=999
        saida = True

print('Você digitou {} números, e a soma deles é {}'.format((cont), (resultado)))
