n = input('Digite algo: ')

print('Ele tem apenas letras? ',(n.isalpha()))
print ('Ele tem apenas numeros?',(n.isnumeric()))
print('Ele é alfanumérico? ',(n.isalnum()))
print('Ele está apenas em Caps? ',(n.isupper()))
print('Ele está apenas em minusculo? ',(n.islower()))
print ('Ele tem maiusculas e minusculas?', (n.istitle()))
print ('O tipo dele é: ',type(n))
