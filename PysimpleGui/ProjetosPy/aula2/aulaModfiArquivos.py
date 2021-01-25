# COMO CRIAR E MODIFICAR ARQUIVOS

preco_celular = [850, 2230, 1500, 3500, 5000]

# 'r' usado para ler algo
# 'w' usado para escrever algo
# 'r+' usado para ler e escrever algo
# 'a' usado para acrescentar algo

'''with open('preco_celular.txt', 'w') as arquivo:
    for valor in preco_celular:
        arquivo.write(str(f'{valor}\n'))'''
'''with open('preco_celular.txt', 'r') as arquivo:
    for valor in arquivo:
        print(str(f'{valor}\n'))'''
with open('preco_celular.txt', 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')
