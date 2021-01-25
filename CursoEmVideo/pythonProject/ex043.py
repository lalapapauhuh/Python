#IMC
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura*altura)
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Status: Abaixo do peso!')
elif imc <= 25:
    print('Status: Peso normal!')
elif imc <= 30:
    print('Status: Sobrepeso!')
elif imc <= 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade Mórbida')