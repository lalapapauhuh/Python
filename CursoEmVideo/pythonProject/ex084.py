#lista composta e analise de dados
pessoa = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    resp = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(pessoa)} pessoa.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]}')
