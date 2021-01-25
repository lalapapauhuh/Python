#analisando a pessoa mais pesada e a mais leve
pesado = 0
leve = float(input('Digite quanto pesa a 1 pessoa: kg '))

for c in range (2,6):
    peso = float(input('Digite quanto pesa a {} pessoa: kg '.format(c)))
    if peso < leve:
        leve = peso
    elif peso > leve and peso > pesado:
        pesado = peso
print('A pessoa mais leve pesa {}kg e a mais pesada pesa {}kg'.format(leve, pesado))