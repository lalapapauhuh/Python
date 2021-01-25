import PySimpleGUI as sg
from random import randint
import os

sg.theme('Black')
   # Criando as janelas e seus layouts
def janela_bemvindo():
    flayout = [
        [sg.Text('BEM-VINDO')],
        [sg.Button('Entrar'), sg.Button('Sair')]
    ]
    # retornando a janela para quem chamou a função (criar variavel para recebe-la)
    return sg.Window('Tela de Inicio', flayout, size=(500,100), element_justification='center', finalize=True)


def janela_cadastro():
    layout = [
    [sg.Text('Digite o nome do funcionário'), sg.Input(size=(30,0), key='-NAME-')],
    [sg.Button('Adicionar')],
    [sg.Text('')],
    [sg.Text('Funcionários Cadastrados: ')],
    [sg.Output(size=(85,20)],
    [sg.Button('Apagar'), sg.Button('Sair')]
    ]
    # retornando a janela para quem chamou a função (criar variavel para recebe-la)
    return sg.Window('Página de Cadastramento', layout=layout, finalize=True)

    # Janela recebendo a primeira tela, a segunda definida como None para nao abrir junto


janela1 = janela_bemvindo()
janela2 = None
    # Loop infinito com os if para cada botao
while True:
    # Atribuindo as variaveis  botao e valor, tudo que acontecer na tela com sg.read_all_windows()
    window, botao, values = sg.read_all_windows()
    if window == janela1 and botao == 'Sair':
        break
    if window == janela1 and botao == 'Entrar':
        janela1.hide()
        janela2 = janela_cadastro()
    if window == janela2 and botao == 'Adicionar':
        ID = randint(123, 9999)
        with open('dados_do_cadastro.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(f'ID {ID}NOME:{os.linesep}')

  # Iniciar/Chamar a função
janela_bemvindo()
