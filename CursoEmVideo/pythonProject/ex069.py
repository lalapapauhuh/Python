#analise de dados
homem = mulher = maior = continuar = 0
while True:
    print('-' * 30)
    print('CADASTRAMENTO DE PESSOAS')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]

    while sexo not in 'MF':
        sexo = str(input('Resposta invalida! tente novamente \n SEXO [M/F] ')).upper()[0].strip()
    if idade > 17:
        maior +=1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher +=1

    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = str(input('Resposta Invalida. Digite apenas Sim ou Não: ')).upper().strip()[0]

print(f'Temos no total {maior} pessoas maiores de 18 anos')
print(f'Ao todo {homem} são homens, e temos {mulher} mulheres com menos de 20 anos.')
