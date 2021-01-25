import PySimpleGUI as sg
import botoes

sg.theme('DefaultNoMoreNagging')

layout = [ 
    [sg.Text('Janela sem bordas, e com botões animados')],
    [sg.Button('', image_data=botoes.botao_confirmar, key='-CONFIRMAR-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    [sg.Button('', image_data=botoes.botao_cancelar, key='-CANCELAR-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
    
]
window = sg.Window('Titulo da janela', layout, grab_anywhere=True)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, '-CANCELAR-'):
        break
window.close()