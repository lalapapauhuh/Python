#Calculo de desconto em %
valor = float(input('Digite o valor do produto: R$ '))
desconto = valor*5/100
vd = valor - desconto
print('O produto custava R${:.2f}. Com 5% de desconto ele passa a custar R${:.2f}'.format(valor, vd))
