def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! "{entrada}" é um preço invalido. Tente novamente!\033[m')
        else:
            valido = True
            return float(entrada)
