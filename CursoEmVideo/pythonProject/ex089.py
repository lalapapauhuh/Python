# Boletim varios alunos
ficha = []
while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"N°.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*30)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno?[999 interrompe]: '))
    if opcao == 999:
        print('Finalizado')
        break
    if opcao <= len(ficha)-1:
        print(f'As notas de {ficha[opcao][0]} são {ficha[opcao][1]}')