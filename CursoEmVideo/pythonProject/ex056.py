#analisador completo
media = 0
nomeH = ''
idadeH = 0
menor = 0
for c in range(1,5):
    print('======== {} pessoa ========'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade
    if c == 1 and sexo == 'M':
        idadeH = idade
        nomeH = nome
    if idade > idadeH and sexo == 'M':
            idadeH = idade
            nomeH = nome
    if idade < 20 and sexo == 'F':
        menor += 1

print('A média de idade é {} anos'.format(media//4))
print('O homem mais velho é o {} e ele tem {} anos'.format(nomeH,idadeH))
print('Nesta lista há {} mulheres com menos de 20 anos'.format(menor))
