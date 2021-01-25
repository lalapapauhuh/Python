def resumo(valor = 0, aumento = 0, reducao = 0):
    cabecalho()
    print(f'Analisando preço: \t{analisar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumento:2}% de aumento: \t{aumento_porcento(valor, aumento)}')
    print(f'{reducao:2}% de redução: \t{reducao_porcento(valor, reducao)}')
    return resumo


def cabecalho():
    titulo = 'RESUMO DO VALOR'
    print('-'*30)
    print(f'{titulo}'.center(30))
    print('-'*30)


def analisar(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def dobro(valor):
    resp = valor*2
    return f'R${resp:.2f}'.replace('.', ',')


def metade(valor):
    resp = valor/2
    return f'R${resp:.2f}'.replace('.', ',')


def aumento_porcento(valor, aumento):
    resp = valor + (valor * aumento)/100
    return f'R${resp:.2f}'.replace('.', ',')


def reducao_porcento(valor, reducao):
    resp = valor - (valor * reducao)/100
    return f'R${resp:.2f}'.replace('.', ',')