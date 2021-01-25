# Calculando a area usando funções
def linha():
    print('-'*30)


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área entre {largura}m x {comprimento}m = {a}m²')


linha()
print('   CALCULANDO A ÁREA   ')
linha()
larg = (float(input('Largura (m): ')))
comp = (float(input('Comprimento (m): ')))
area(larg, comp)
