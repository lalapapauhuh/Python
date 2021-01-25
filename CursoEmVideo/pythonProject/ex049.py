#tabuada
n = int(input('Digite um número: '))
print('A tabuada do {} é:' .format(n))
print('='*20)
for c in range(1,11):
    print('{:2} * {:2} = {:2}'.format(n ,c, c*n))
