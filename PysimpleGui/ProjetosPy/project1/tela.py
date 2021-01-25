import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        sg.theme('DarkBlack') 
        layout = [
            [sg.Text('Nome:',size=(5,0)), sg.Input(size=(20,0), key='nome')],
            [sg.Text('Idade:',size=(5,0)), sg.Input(size=(20,0), key='idade')],
            [sg.Text('Selecione o tipo de email abaixo: ')],
            [sg.Radio('Gmail',"RADIO1", key='gmail'), sg.Radio('Outlook',"RADIO1", key='outlook'), sg.Radio('Yahoo',"RADIO1", key='yahoo')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h',size=(15,20), key='slider')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(20,8))]

            
        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)


    def Iniciar(self):
        while True:
             # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail?: {gmail}')
            print(f'Outlook?: {outlook}')
            print(f'Yahoo?: {yahoo}')
           


tela = TelaPython()
tela.Iniciar()