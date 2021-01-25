# função com parametros opcionais, jogador de futebol e gols
def carreira(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol}(s) no campeonato.')

jogador = str(input('Nome do jogador: '))
nGols = str(input('Número de gols: '))
if nGols.isnumeric():
    nGols = int(nGols)
else:
    nGols = 0

if jogador.strip() == '':
    carreira(gol=nGols)
else:
    carreira(jogador, nGols)