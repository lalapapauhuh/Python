from ex108 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {(moeda.money(preco))} é {moeda.money(moeda.metade(preco))}')
print(f'O dobro de {moeda.money(preco)} é {moeda.money(moeda.dobro(preco))}')
print(f'Aumentando 10% de {moeda.money(preco)} temos {moeda.money(moeda.dez_porcento(preco))}')
print(f'Reduzindo 15% de {moeda.money(preco)} temos {moeda.money(moeda.quinze_porcento(preco))}')