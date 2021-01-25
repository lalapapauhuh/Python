banco = cedulas = resto50 = resto20= resto10=0
valor = int(input('Digite o valor do saque R$: '))
while True:
    if valor >= 50:
        cedulas = valor//50
        resto50 = valor % 50
        print('Total de notas de R$50: {}'.format(cedulas))
        print('sobrou {}'.format(resto50))
        if resto50 == 0:
            break
        elif resto50 >= 20:
            cedulas = resto50 // 20
            resto20 = resto50 % 20
            print('Total de notas de R$20: {}'.format(cedulas))
            print('sobrou {}'.format(resto20))
            if resto20 == 0:
                break
        elif resto20 >= 10 or resto50 >= 10 :
            if resto20 == 0:
                resto20 = resto50
            cedulas = resto20//10
            resto10 = resto20 % 10
            print('Total de notas de R$10: {}'.format(cedulas))
            print('sobrou {}'.format(resto10))
            if resto10 == 0:
                break
        elif resto10 >= 1 or resto20 >= 1:
            if resto10 == 0:
                resto10 = resto20
            cedulas = resto10 // 1
            print('Total de notas de R$10: {}'.format(cedulas))
            break
print('fim')