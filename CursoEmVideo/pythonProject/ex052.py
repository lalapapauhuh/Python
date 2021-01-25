#numeros primos
n = int(input('Digite um número: '))
primo = 0
total = 0
for cont in range(1,n):
    primo = n%cont
    if primo == 0:
        total += 1

if total == 1:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))