# Unindo dicionarios e listas

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Resposta Invalida. Por favor responda novamente')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
           break
        print('Resposta invalida! Tente novamente')
    if resposta == 'N':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
media = soma/len(galera)
print(f'A média de idade é {media:5.2f}anos')
print('As mulheres cadastradas foram: ', end='')
for pess in galera:
    if pess['sexo'] == 'F':
     print(f'{pess["nome"]} ', end='')
print()
print('As pessoas que tem idade acima da media são: ')
for pess in galera:
    if pess['idade'] > media:
        print(f'{pess["nome"]}' , end='')
print()
