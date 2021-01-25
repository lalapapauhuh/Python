#formar um triângulo
print('Analisa se forma um triângulo')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 +r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo!!!')
else:
    print('Essas restas não podem formar um triântulo!!!')