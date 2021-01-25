#valores unicos em uma lista
lista = []
while True:
    novo = int(input('Digite um valor: '))
    if novo in lista:
        print('Este valor já foi adicionado!')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(novo)
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
print('=-'*20)
lista.sort()
print(f'Você digitou os valores {lista}')
