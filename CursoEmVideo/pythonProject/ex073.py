br = ('Atletico Mineiro', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Bahia','Sport',
      'Corinthians', 'Fortaleza', 'Ceará', 'Atletico Goianiense', 'Bragantino', 'Vasco', 'Athletico Paranaense', 'Coritiba',
      'Botafogo','Goias')
print(f'Os primeiros colocados são: {br[0:5]}\n')
print(f'Os times rebaixados são: {br[-4:]}\n')
print('O Bragantino está na posição: {}\n'.format(br.index('Bragantino')+1))
print('Os times participantes esse ano são:')
print(sorted(br))