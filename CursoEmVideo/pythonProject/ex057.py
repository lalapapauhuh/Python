#validação de dados
nome = str(input('Digite seu nome: '))

sexo = str(input('SEXO [M/F] ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Resposta invalida! tente novamente \n SEXO [M/F] ')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(sexo))


idade = int(input('Digite sua idade: '))

print('Nome: {} \n Idade: {}\n Sexo: {}'.format(nome, idade, sexo))