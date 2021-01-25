# Janela unica

import PySimpleGUI as sg

event, values = sg.Window('Tela de Login',
    [[sg.T('Username:'), sg.In(key='-NICK-')],
    [sg.Submit('OK'), sg.B('Cancelar')]]).read(close=True)

usuario = values['-NICK-']
sg.popup('Seu nick é ', usuario)