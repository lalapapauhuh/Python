#tabuada 3.0
valor = cont = 1
while True:
    cont = 1
    print('-'*30)
    valor = int(input('Digite o valor da tabuada: '))
    print('-' * 30)
    if valor > 0:
        while cont <= 10:
              print(f'{valor:2} * {cont:2} = {valor*cont}')
              cont += 1
    else:
        print('Fechando programa...')
        print('Fim')
        break
print('-'*30)