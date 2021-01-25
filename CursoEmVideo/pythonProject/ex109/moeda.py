
def metade(valor = 0, format = False):
    resp = valor/2
    return resp if format is False else money(resp)


def dobro(valor = 0, format = False):
    resp = valor*2
    return resp if format is False else money(resp)


def dez_porcento(valor = 0, format = False):
    resp = valor + (valor*10)/100
    return resp if format is False else money(resp)


def quinze_porcento(valor = 0, format = False):
    resp = valor - (valor*15)/100
    return resp if format is False else money(resp)


def money(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')