#lista de preços com tupla

precos = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 5.00,
          'Transferidor', 4.00,
          'Compasso', 9.99,
          'Canetas', 12.00,
          'Mochila', 89.90,
          'Livro', 54.90)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
         print(f'{precos[pos]:.<30}', end= ' ')
    else:
        print(f'R$ {precos[pos]:>5.2f}')
