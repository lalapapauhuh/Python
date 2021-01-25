# Tela que abre e fecha
# Auto gerador de key

import PySimpleGUI as sg

sg.theme('Black')

layout = [
    [sg.Text('Minha tela inicial')], # linha 1
    [sg.Input()],  # linha2
    [sg.Submit('Entrar'), sg.Cancel()], # linha 3 
]
window = sg.Window('Título da janela', layout)

events, values = window.read()
window.close()

text_input = values[0]  # Como so tem um input, é o unico argumento por isso 0.
#  Se houvesse mais teriam 1, 2,3 (items em um dicionario)
sg.popup('Você digitou', text_input)

'''
AQUI MUDA A KEY QUE ESTÁ DEFINIDA, POREM MESMO RESULTADO FINAL
sg.theme('Black')

layout = [
    [sg.Text('Minha tela inicial')], # linha 1
    [sg.Input(key='-TEXTO-')],  # linha2
    [sg.Submit('Entrar'), sg.Cancel()], # linha 3 
]
window = sg.Window('Título da janela', layout)

events, values = window.read()
window.close()

text_input = values['-TEXTO-']
sg.popup('Você digitou', text_input)

'''