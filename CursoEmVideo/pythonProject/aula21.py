# Funções part 2

# Interactive Help
'''help(input)
print(input.__doc__)

def contador(i,f,p):
    """
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p:Passo da contagem (de quanto em quanto)
    :return: Não possui retorno
    """
    while i <= f:
        print(f'{i}', end=' ')
        i += p
    print('Fim')

contador(2, 10, 2)
print(contador.__doc__)'''

# Argumentos opcionais
'''
def somar (a, b, c=0): # c=0 se o C não for passado na chamada, ele recebe 0 e evita o erro
    s = a + b+ c
    print(f'A soma vale {s}')

somar(2, 3, 5)
somar(8, 4)
'''

# Escopo de variaveis
#Local que a variavel vai existir, e onde ela deixa de existir
'''def test():
    x = 8
    print(f'Na função test, n vale {n}')
    print(f'Na função test, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')# no programa principal X não existe
# x é uma variavel local da função test, ja N é uma variavel global.
test()'''
'''def funcao():
   #global n1   sem o #
    n1 = 5
    print(f'N1 dentro vale {n1}')
n1 = 2
funcao()
print(f'N1 fora vale {n1}')
# Para n1 valer 5 dentro e fora usar 'global n1' entao ele modifica o valor da variavel pra 5
dentro e fora da função
'''

# Retorno de resultados
'''def somar (a=0, b=0, c=0):
    s = a + b+ c
    return s

result1 = somar(2, 3, 5)
result2 =somar(8, 4)
result3 = somar(6)
print(f'Os resultados foram {result1}, {result2} e {result3}')'''

# praticando
'''def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f*= cont
    return f


n1 = int(input('Digite um número: '))
print(f'O fatorial de {n1} é {fatorial(n1)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1} {f2} e {f3}')'''

'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print(f'{num } é par')
else:
    print(f'{num} é impar')'''
