import PySimpleGUI as sg

sg.theme('Black')

layout = [
    [sg.Text('Temas')],
    [sg.Text('Escolha um tema')],
    [sg.Listbox(values =sg.theme_list(), size=(20,12), key='lista', enable_events=True)],
    [sg.Button('Confirmar'), sg.Button('Sair')]
]

window = sg.Window('Temas', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    sg.theme(values['lista'][0])
    sg.popup_get_text('Este é o tema {}'.format(values['lista'][0]))