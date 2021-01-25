# tuplas ()
# listas []
# dicionarios {}

''' 
dados = dict(
dados = { 'nome: 'Cássio,
          'idade: 23
 }
print(dados['nome'])
dados['sexo'] = 'M' # Adicionar novo elemento no dicionario

# Deletando elementos
del dados['idade']
'''

# EXEMPLO 2
'''filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
# values/keys/items
print(filme.values()) # dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme.keys()) # dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items()) # dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# parecido com enumerates
for key, value in filme.items():
    print(f'O {key} é {value}') # O titulo é Star Wars / O ano é 1977 / ...
'''
# EXEMPLO 3 LISTA + DICIONARIOS
    #Uma lista chamada brasil, com varios dicionarios, sendo eles os estados
'''brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'Sp'}
estado2 = {'uf': 'Rio de Janeiro', 'sssigla': 'Rj'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf']) #print São Paulo'''

# EXEMPLO 4 Usando for
estado = {}
brasil = []
for cont in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # .copy() é parecido com o [:] de listas
for est in brasil:
    for key, valor in est.items():
        print(f'O campo {key} tem valor {valor}')
