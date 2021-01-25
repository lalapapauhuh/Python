def soma (n1, n2):
    resultado = n1 + n2
    return resultado


def subtrai (n1, n2):
    resultado = n1 - n2
    return resultado


def multiplica (n1, n2):
    resultado = n1 * n2
    return resultado


def divide (n1, n2):
    resultado = n1 / n2
    return resultado


def operacao():
    print('  Simbolos operacionais\n +  -  *  /')
    sinal = str(input('Digite o símbolo da operação que você quer realizar: '))
    if sinal == '+':
        return soma
    elif sinal == '-':
        return subtrai
    elif sinal == '*':
        return multiplica
    elif sinal == '/':
        return divide


numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
conta = operacao()
resposta = conta(numero1, numero2)
print(f'{resposta}')