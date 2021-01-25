from ex109 import moeda

preco = float(input('Digite o preço: R$ '))
while True:
    condicao = str(input('Deseja formatado como moeda?[S/N]: ')).upper().strip()[0]
    if condicao in 'SN':
        if condicao == 'S':
            formatar = True
            break
        else:
            formatar = False
            break
print('-='*30)
print(f'A metade de {moeda.money(preco)} é {moeda.metade(preco, formatar)}')
print(f'O dobro de de {moeda.money(preco)} é {moeda.dobro(preco, formatar)}')
print(f'Aumentando 10% de {moeda.money(preco)} temos {moeda.dez_porcento(preco, formatar)}')
print(f'Reduzindo 15% de {moeda.money(preco)} temos {moeda.quinze_porcento(preco, formatar)}')
