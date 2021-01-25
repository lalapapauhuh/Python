import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text('Preencha seus dados abaixo', font=('Helvetica', 12))],

    [sg.Text('Nome', size=(7,0), font=('Helvetica', 11)), 
     sg.Input(size=(35,1))],

    [sg.Text('Endereço', size=(7,0), font=('Helvetica', 11)), 
     sg.Input(size=(35,1))],

    [sg.Text('Telefone', size=(7,0), font=('Helvetica', 11)), 
     sg.Input(size=(35,1))],

    [sg.Submit('Enviar', font=('Helvetica', 10)), sg.Button('Cancelar', font=('Helvetica', 10))]
]
window = sg.Window('Tela de Cadastro', layout)
event, values = window.read()
window.close()

if event == 'Enviar':
    print(f'Nome: {values[0]}\nEndereço: {values[1]}\nTelefone: {values[2]}')
    sg.popup('Os dados foram salvos com sucesso')

        
