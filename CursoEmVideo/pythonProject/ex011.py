#pintando a parede
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura*largura
tinta = area/2
print('Sua parede tem {}x{} a area dela é de {:.2f}m²\nSerá necessário {:.2f}L de tinta para pinta-lá'.format(altura, largura, area, tinta))

