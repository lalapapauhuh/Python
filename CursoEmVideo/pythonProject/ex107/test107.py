# Treinando uso de modulos
from ex107 import moeda


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {(preco)} é {moeda.metade(preco)}')
print(f'O dobro de {(preco)} é {preco}')
print(f'Aumentando 10% de {preco} temos {moeda.dez_porcento(preco)}')
print(f'Reduzindo 15% de {preco} temos {moeda.quinze_porcento(preco)}')