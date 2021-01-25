#criando uma matriz
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor para posição [{linha},{coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') #printa cada item da matriz
    print() #quebra a linha
