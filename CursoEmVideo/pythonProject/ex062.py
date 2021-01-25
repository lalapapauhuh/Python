#super progressão aritmetica 3.0
print('='*8,'Progressão aritmetica', '='*8 )
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmetica: '))
contador = 0
novo = 0
limite = 10

while contador < limite:
    print(n, end=' ')
    n = n+r
    contador += 1
    if contador >= limite:
        novo = int(input('\nQuantos termos mais você quer mostrar? '))
        limite = limite + novo

print('Finalizando... Total de termos mostrados {}'.format(limite))
