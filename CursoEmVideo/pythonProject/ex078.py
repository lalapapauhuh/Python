valores = []
maior = menor = 0
pmaior = pmenor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont+1} valor: ')))
    if cont == 0:
        maior = menor = valores[0]
    if valores[cont] > maior:
        maior = valores[cont]
    if valores[cont] < menor:
        menor = valores[cont]

print(f'Os valores digitados foram {valores} ')
print(f'O maior valor foi o {maior} na posição', end=' ')
for indice, v in enumerate(valores):
    if valores[indice] == maior:
        print(indice)
print(f'O menor valor foi o {menor} na posição', end=' ')
for indice, v in enumerate(valores):
    if valores[indice] == menor:
        print(indice, end=' ')
