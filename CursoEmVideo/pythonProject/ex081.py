#extraindo dados de uma lista
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Continuar? [S/N]: ')).upper()[0].strip()
    if resp =='N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores digitados são: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')