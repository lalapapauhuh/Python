import random

animais = {'leão': 'lion', 'tigre': 'tigre', 'baleia': 'baleine', 'cachorro': 'chien', 'camundongo': 'souris', 'borboleta': 'papillon', 'cadela': 'chienne', 'mosca': 'mouche', 'elefante': 'éléphant',
'gata': 'chatte', 'porco': 'cochon', 'golfinho': 'dauphin', 'gato': 'chat', 'macaco': 'singe', 'formiga': 'fourmi', 'pássaro': 'oiseau', 'tubarão': 'requin', 'urso': 'ours', 'cavalo': 'cheval', 'aranha': 'araignée',
'lobo': 'loup', 'tartaruga': 'tortue', 'serpente': 'serpent', 'pato': 'canard'
}

def titulo(msg):
    print('-'*30)
    print(f'{msg}'.center(30))
    print('-'*30)

titulo('Animais Frances')
while True:
    escolha = random.choice(list(animais.keys()))
    resposta = str(input(f'Como se diz {escolha} em FR: '))
    traducao = animais[escolha]
    if resposta == traducao:
        print('\033[1;32mAcertou!!!\033[m')

    else:
        print(f'\033[1;31mErrou. O certo seria {traducao}\033[m')
        break
