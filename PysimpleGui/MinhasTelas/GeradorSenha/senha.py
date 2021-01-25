import random
import PySimpleGUI as sg


class SenhaGerar:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Nome', size=(10,1)), sg.Input(size=(40,1), key='nome')],
            [sg.Text('Email', size=(10,1)), sg.Input(size=(40,1), key='email')],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_caracters', default_value=1, size=(3,1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarando janela
        self.janela = sg.Window('Gerador de Senhas',layout)


    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                #self.salvar_senha(nova_senha, valores)


    def gerar_senha(self, valores):
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç1234567890_.+-'
        aleatorio = random.choices(caracteres,k=int(valores['total_caracters']))
        new = ''.join(aleatorio)
        return new


   # def salvar_senha
        


gerar = SenhaGerar()
gerar.Iniciar()