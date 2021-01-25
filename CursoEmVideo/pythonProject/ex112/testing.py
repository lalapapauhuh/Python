from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dados

preco = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 50, 25)
