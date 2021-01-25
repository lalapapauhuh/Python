#aluguel de carros
dia = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos km foram rodados? '))
valor_km = (km*0.15)
valor_dia = (dia*60)
print('O total a pagar é de R${:.2f}'.format(valor_dia + valor_km))
