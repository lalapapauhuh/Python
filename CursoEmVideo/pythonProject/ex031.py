#valor da passagem
km = float(input('Digite a distância do seu destino: '))
if km <= 200:
    print('O valor da passagem é: R$ {:.2f}'.format(km*0.50))
else:
    print('O valor da passagem é: R$ {:.2f}'.format(km*0.45))