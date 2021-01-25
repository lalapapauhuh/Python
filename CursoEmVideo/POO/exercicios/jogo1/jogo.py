from funcoes import titulo
from funcoes import menu
from funcoes import novo
from funcoes import jogar

titulo('ANIMAIS EM FR ')
menu()

while True:
    opcao = int(input('Digite uma das opções: '))
    if opcao == 3:
        break
    elif opcao == 2:
        pt = str(input('Digite a palavra nova em Pt-Br : '))
        fr = str(input('Digite agora ela em Fr: '))
        
        print(f'Palavra: {pt}\nTradução: {fr}')
        novo(pt, fr)
        break
    elif opcao == 1:
        jogar()
        break
    else: 
        print('Por favor digite uma opção valida!')
