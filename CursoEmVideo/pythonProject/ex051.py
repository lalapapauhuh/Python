#razao aritmetica
print('='*8,'Progressão aritmetica', '='*8 )
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
contador = (r * 10)+n

for c in range(n, contador, r):
        print(n, end=' ')
        n= n+r
print('\nFim')
