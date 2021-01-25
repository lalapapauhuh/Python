#Calculo de aumento salarial
salario = float(input('Qual salário atual do funcionário? R$ '))
novo = (salario*15/100)
print('O novo salário com 15% de aumento é R$ {:.2f}'.format(salario+novo))