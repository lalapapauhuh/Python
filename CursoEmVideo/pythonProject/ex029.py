#velocidade do carro
print('Velocidade máxima permitida 80km/h')
velo = float(input('Digite a velocidade do carro: Km/h '))
if velo > 80:
    valor = velo - 80
    print('O carro estava {:.2f} Km/h acima do limite. Então será multado em R$ {:.2f}.'.format(valor,(valor*7)))
else:
    print('Velocidade dentro do limite.')