#numero por extenso
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))

if num >= 0 and num <=20:
    print(f'Você digitou {numero[num]}')
else:
    while True:
        num = int(input('Invalido. Digite novamente um número entre 0 e 20: '))
        if num >= 0 and num <= 20:
            print(f'Você digitou {numero[num]}')
            break
