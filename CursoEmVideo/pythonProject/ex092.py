# CADASTRO DE TRABALHO
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dados['CTPS'] != 0:
    dados['contratacao'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - nascimento
print('-='*30)
for key, valor in dados.items():
    print(f' _ {key} tem o valor {valor}')


