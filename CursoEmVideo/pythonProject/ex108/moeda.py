def metade(valor = 0):
    resp = valor/2
    return resp


def dobro(valor = 0):
    resp = valor*2
    return resp


def dez_porcento(valor = 0):
    resp = valor + (valor*10)/100
    return resp


def quinze_porcento(valor = 0):
    resp = valor - (valor*15)/100
    return resp


def money(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')