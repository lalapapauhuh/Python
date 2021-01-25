# CADASTRO DE JOGADOR 2.0 
jogador = {}
gols = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    for jogo in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {jogo+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Responda apenas Sim ou Não')
    if resp == 'N':
        break
print('-'*40)
for key, valor in enumerate(time):
    print(f'{key:>3}')
    for dado in valor.values():
        print(f'{str(dado):<15}')
    print()

'''print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for indc, valor in enumerate(jogador['gols']):
    print(f'   _ Na partida {indc+1}, fez {valor} gols.')
print(f' No total foram {jogador["total"]} gols')'''
