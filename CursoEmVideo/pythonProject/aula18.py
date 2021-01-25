'''pessoas = [['pedro', 25], ['maria', 19], ['joão', 32]]
print(pessoas[1][1]) #print mostra 19'''

'''teste = list()
teste.append('Cássio')
teste.append(23)
galera = list()
galera.append(teste[:]) #salva os dados anteriores [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

galera = []
dados = []
maior = menor = 0
for cont in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #passando os dados para lista galera
    dados.clear() #apagando oq estava salvo em dados

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade, e {menor} menores de idade')