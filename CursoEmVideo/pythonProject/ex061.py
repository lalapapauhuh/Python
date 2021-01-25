#progressão aritmetica 2.0
print('='*8,'Progressão aritmetica', '='*8 )
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
contador = 0

while contador < 10:
    print(n, end=' ')
    n = n+r
    contador += 1