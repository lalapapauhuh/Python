#maior e menor valores e media
fim = 'S'
contador = media = soma = 0
maior = menor = test = 0

while fim in 'S':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    fim = str(input('Quer continuar? [S/N]: ')).upper().strip()

media = soma / contador
print(f'A média dos valores acima é {media:.2f}, o maior dos números é {maior} e o menor deles é {menor}')