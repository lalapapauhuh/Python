#fibonacci
print('====== Fibonacci =======')
termos = int(input('Quantos termos você quer mostrar? '))
f1 = 0
f2 = 1
cont = 2
print(f1, end=' ')

while cont <= termos:
    aux = f1
    f1 = f1 + f2
    print(f1, end=' ')
    f2 = aux
    cont += 1




