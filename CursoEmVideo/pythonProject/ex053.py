# detector de palindromo
frase = str(input('Digite uma frase: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
inverte =''

for letra in range(len(junto)-1,-1,-1):
    inverte += junto[letra]
print('O inverso de {} é {}'.format(junto, inverte))
if junto == inverte:
    print('A frase é um palíndromo! ')
else:
    print('A frase não é um palíndromo')
