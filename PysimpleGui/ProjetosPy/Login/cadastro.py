from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Dark Grey 12')
layout = [
    [sg.Text('Usuário',size=(8,0)), sg.Input(key='usuario', size=(25,0))],
    [sg.Text('Senha', size=(8,0)), sg.Input(key='senha', password_char='*', size=(25,0))],
    [sg.Checkbox('Salvar senha?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de login', layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'cassio645' and valores['senha'] == 1234:
            print('Bem vindo Cassio')
        