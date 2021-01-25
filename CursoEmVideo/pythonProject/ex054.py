#verifica quantos sao maior de idade e qnts são menores
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nascimento = int(input('Digite a idade da {} pessoa: '.format(c)))
    idade = atual-nascimento
    if idade >= 18:
        maior += 1
    else:
        menor +=1
print('Analisando as idades acima {} são maiores de idade e {} são menores de idade'.format(maior, menor))