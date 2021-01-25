banco = cedulas = resto50 = resto20= resto10=0
cores = {'limpa': '\033[m',
         'branco': '\033[7m'
}
print('='*40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('='*40)
valor = int(input('Digite o valor do saque R$: '))
while True:
        if valor >= 50:
           cedulas = valor//50
           resto50 = valor % 50
           print('Notas de R$50: {}'.format(cedulas))
        if resto50 >= 20:
            cedulas = resto50 // 20
            resto20 = resto50 % 20
            print('Notas de R$20: {}'.format(cedulas))
        if resto20 >= 10:
           cedulas = resto20 // 10
           resto10 = resto20 % 10
           print('Notas de R$10: {}'.format(cedulas))
        elif resto50 >=10:
           cedulas = resto50 // 10
           resto10 = resto50 % 10
           print('Notas de R$10: {}'.format(cedulas))
        if resto10 >= 1:
            cedulas = resto10 // 1
            print('Notas de R$1: {:2}'.format(cedulas))
        elif resto20 >= 10:
            cedulas = resto20 // 10
            print('Notas de R$1: {:2}'.format(cedulas))
        elif resto50 >=1:
            cedulas = resto50 // 1
            print('Notas de R$1: {:2}'.format(cedulas))
        break
print('-'*40)
print('{}Finalizando saque...{}'.format(cores['branco'], cores['limpa']))
print('Tenha um bom dia!')
