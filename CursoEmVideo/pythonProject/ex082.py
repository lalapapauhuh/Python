#dividindo valores em varias listas
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

for i, v in enumerate(lista): # i = indice do for/ v = valor digitado na (lista)
 if v % 2 == 0 :
     par.append(v)
 else:
     impar.append(v)
print('-='*30)
print(f'A lista completa é: {lista}')
print(f'Os pares digitados: {par}')
print(f'Os impares digitados: {impar}')