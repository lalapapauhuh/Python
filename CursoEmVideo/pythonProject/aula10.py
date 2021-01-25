n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >= 6:
    print('Nota: {} Aluno aprovado!!'.format(m))
else:
    print('Nota: {} Aluno reprovado!!'.format(m))