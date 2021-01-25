#aprovando emprestimo
from time import sleep
cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'pretob': '\033[7;30m'
         }

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual valor do seu salário? R$ '))
anos = int(input('Em quantos anos você deseja financiar? '))
prestacao = casa/(anos*12) #anos virando meses
print('As prestações serão de R$ {:.2f}'.format(prestacao))

num = salario*30/100 #calculando 30% do salario
print('{}ANALISANDO...{}'.format(cores['pretob'], cores['limpar']))
sleep(2) #faz o analisar ficar por alguns segundos

if prestacao > num:

    print('{}Emprestimo negado{}'.format(cores['vermelho'], cores['limpar']))

else:
    print('{}Emprestimo aprovado{}'.format(cores['verde'], cores['limpar']))