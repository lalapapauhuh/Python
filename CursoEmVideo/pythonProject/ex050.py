#somando somente os pares
soma = 0
for c in range(1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n%2 == 0:
        soma = soma + n
    c = c+1
print('A soma dos pares é {}'.format(soma))