palavras = ('ANDAR', 'DIGITAR', 'TECLAR', 'COMPUTADOR','TECLADO', 'MOUSE', 'CELULAR', 'ROTEADOR')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
           print(letra, end=' ')