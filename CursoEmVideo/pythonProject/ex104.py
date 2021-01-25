# Validando entrada de dados
def leiaInt(msg):
    cor = {
        'limpar': '\033[m',
        'vermelho': '\033[31m'
    }
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cor["vermelho"]}Erro! {n} não é um número inteiro! Tente novamente.{cor["limpar"]}')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
