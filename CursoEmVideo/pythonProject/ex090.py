# Dicionario python
aluno = {}
aluno ['nome'] = str(input('Nome: '))
aluno ['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação']= 'Aprovado!'
elif  aluno['media'] >= 5:
    aluno['situação']= 'Recuperação!'
else: 
    aluno['situação']= 'Reprovado!'


for key, valor in aluno.items():
    print(f'{key} é igual a {valor}')