# Função escreva adaptavel

def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva('oi')
escreva('Curso de python do youtube 2020')
escreva('testando função')
