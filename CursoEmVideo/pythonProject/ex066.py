num = cont = soma = 0
while True:
    num = int(input('Digite o valor [para sair digite 999]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Foram digitados {} números e a soma deles é {}'.format(cont, soma))
