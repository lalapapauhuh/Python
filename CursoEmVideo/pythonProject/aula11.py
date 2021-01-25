#cores ANSI
'''style
0 - sem estilo
1 - negrito
4 - sublinhado
7 - negativo
'''

'''cores das fontes
30- branco/ 31- vermelho/ 32- verde/ 33- amarelo/ 34- azul
35- roxo/ 36- ciano/ 37- cinza
'''

'''cores background
40- branco/ 41- vermelho/ 42- verde/ 43- amarelo/ 44- azul
45- roxo/ 46- ciano/ 47- cinza
'''
# print( ' \033[style; font color; backgroundCORmTEXTO...\033[m')
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[0;30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;40mTeste\033[m')# preto e  branco



'''a = 3
b = 5
print('Os valores são \033[7;32m{}\033[m e \033[7;31m{}\033[m!!!'.format(a, b))'''
