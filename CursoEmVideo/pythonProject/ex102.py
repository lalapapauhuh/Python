#fatorial mostrando ou não
def fatorial(n, show=False):
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont , end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


numero = int(input('Digite um número: '))
mostrar = str(input('Caso queira ver o calculo digite Sim: ')).upper().strip()[0]
if mostrar == 'S':
    mostrar = True
print(fatorial(numero, mostrar))