#aumento de salario
salario = float(input('Digite o valor do salário: R$ '))
if salario > 1250.00:
    novo = salario + (salario*10/100)
    print('Seu salário agora é R$ {:.2f}'.format(novo))
else:
    novo = salario + (salario*15/100)
    print('Seu salário agora é R$ {:.2f}'.format(novo))