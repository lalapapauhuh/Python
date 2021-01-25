# CADASTRO DE JOGADOR
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for jogo in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na partida {jogo+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)

for key, valor in jogador.items():
    print(f'{key} tem o valor: {valor}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for indc, valor in enumerate(jogador['gols']):
    print(f'   _ Na partida {indc+1}, fez {valor} gols.')
print(f' No total foram {jogador["total"]} gols')
