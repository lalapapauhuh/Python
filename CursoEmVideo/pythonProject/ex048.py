#a soma de todos os impares multiplos de 3 entre 1 e 500
print('Somando Impares multiplos de 3. Entre 1 e 500')
num = 0
cont = 0
for c in range(3,501,3):
    if c % 2 != 0:
      num += c
      cont += 1

print('A soma deles é {}. Foram somados {} valores'.format(num, cont))
print('fim')