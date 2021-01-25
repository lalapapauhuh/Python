#classificando triangulos
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 +r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('Essas retas formam um triângulo:', end=" ")
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1!= r2 != r3 and r1 != r3:
        print('Escaleno')
    else:
        print ('Isósceles')

else:
    print('Essas restas não podem formar um triântulo!!!')