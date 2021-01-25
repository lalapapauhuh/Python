# Tela que não fecha sozinha
import PySimpleGUI as sg
sg.list_of_look_and_feel_values()
sg.change_look_and_feel('Reddit') 


layout = [
    [sg.Text('Janela que não fecha')],
    [sg.Input(key='-IN-')],
    [sg.Submit('Ler'), sg.Exit('Sair')]
]

window = sg.Window('Janela Aberta', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    
    if event == 'Ler':
        window['-IN-'].update('')
        
window.close()