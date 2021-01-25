#usando matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contador = maior = soma = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 ==0:
            contador += matriz[l][c]
    print()

print('-='*30)
print(f'A soma de todos os pares é: {contador}')
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores da terceira coluna são: {soma}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')